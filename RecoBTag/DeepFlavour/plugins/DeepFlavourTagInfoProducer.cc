
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "DataFormats/BTauReco/interface/ShallowTagInfo.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "DataFormats/DeepFormats/interface/DeepFlavourTagInfo.h"
#include "DataFormats/DeepFormats/interface/DeepFlavourFeatures.h"

#include "RecoBTag/DeepFlavour/interface/jet_features_converter.h"
#include "RecoBTag/DeepFlavour/interface/btag_features_converter.h"
#include "RecoBTag/DeepFlavour/interface/sv_features_converter.h"
#include "RecoBTag/DeepFlavour/interface/n_pf_features_converter.h"
#include "RecoBTag/DeepFlavour/interface/c_pf_features_converter.h"

#include "RecoBTag/DeepFlavour/interface/TrackInfoBuilder.h"
#include "RecoBTag/DeepFlavour/interface/sorting_modules.h"



class DeepFlavourTagInfoProducer : public edm::stream::EDProducer<> {

  public:
	  explicit DeepFlavourTagInfoProducer(const edm::ParameterSet&);
	  ~DeepFlavourTagInfoProducer();

	  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  private:
    typedef std::vector<reco::DeepFlavourTagInfo> DeepFlavourTagInfoCollection;
    typedef reco::VertexCompositePtrCandidateCollection SVCollection;
    typedef reco::VertexCollection VertexCollection;
    typedef edm::View<reco::ShallowTagInfo> ShallowTagInfoCollection;

	  virtual void beginStream(edm::StreamID) override {}
	  virtual void produce(edm::Event&, const edm::EventSetup&) override;
	  virtual void endStream() override {}

    
    const double jet_radius_;

    edm::EDGetTokenT<edm::View<reco::Jet>>  jet_token_;
    edm::EDGetTokenT<VertexCollection> vtx_token_;
    edm::EDGetTokenT<SVCollection> sv_token_;
    edm::EDGetTokenT<ShallowTagInfoCollection> shallow_tag_info_token_;
    edm::EDGetTokenT<edm::ValueMap<float>> puppi_value_map_token_;
    edm::EDGetTokenT<edm::ValueMap<int>> pvasq_value_map_token_;

    bool use_puppi_value_map_;
    bool use_pvasq_value_map_;
    
};

DeepFlavourTagInfoProducer::DeepFlavourTagInfoProducer(const edm::ParameterSet& iConfig) :
  jet_radius_(iConfig.getParameter<double>("jet_radius")),
  jet_token_(consumes<edm::View<reco::Jet> >(iConfig.getParameter<edm::InputTag>("jets"))),
  vtx_token_(consumes<VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
  sv_token_(consumes<SVCollection>(iConfig.getParameter<edm::InputTag>("secondary_vertices"))),
  shallow_tag_info_token_(consumes<ShallowTagInfoCollection>(iConfig.getParameter<edm::InputTag>("shallow_tag_infos"))),
  use_puppi_value_map_(false),
  use_pvasq_value_map_(false)
{
  produces<DeepFlavourTagInfoCollection>();

  const auto & puppi_value_map_tag = iConfig.getParameter<edm::InputTag>("puppi_value_map");
  if (!puppi_value_map_tag.label().empty()) {
    puppi_value_map_token_ = consumes<edm::ValueMap<float>>(puppi_value_map_tag);
    use_puppi_value_map_ = true;
  }

  const auto & pvasq_value_map_tag = iConfig.getParameter<edm::InputTag>("pvasq_value_map");
  if (!pvasq_value_map_tag.label().empty()) {
    pvasq_value_map_token_ = consumes<edm::ValueMap<int>>(pvasq_value_map_tag);
    use_pvasq_value_map_ = true;
  }

}


DeepFlavourTagInfoProducer::~DeepFlavourTagInfoProducer()
{
}

void DeepFlavourTagInfoProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions)
{
}

void DeepFlavourTagInfoProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  auto output_tag_infos = std::make_unique<DeepFlavourTagInfoCollection>();

  edm::Handle<edm::View<reco::Jet>> jets;
  iEvent.getByToken(jet_token_, jets);

  edm::Handle<VertexCollection> vtxs;
  iEvent.getByToken(vtx_token_, vtxs);
  // reference to primary vertex
  const auto & pv = vtxs->at(0);

  edm::Handle<SVCollection> svs;
  iEvent.getByToken(sv_token_, svs);

  edm::Handle<ShallowTagInfoCollection> shallow_tag_infos;
  iEvent.getByToken(shallow_tag_info_token_, shallow_tag_infos);

  edm::Handle<edm::ValueMap<float>> puppi_value_map;
  if (use_puppi_value_map_) { 
    iEvent.getByToken(puppi_value_map_token_, puppi_value_map);
  }

  edm::Handle<edm::ValueMap<int>> pvasq_value_map;
  if (use_pvasq_value_map_) { 
    iEvent.getByToken(pvasq_value_map_token_, pvasq_value_map);
  }

  edm::ESHandle<TransientTrackBuilder> track_builder; 
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", track_builder);

  for (std::size_t jet_n = 0; jet_n <  jets->size(); jet_n++) {

    // create data containing structure
    deep::DeepFlavourFeatures features;

    // reco jet reference (use as much as possible)
    const auto & jet = jets->at(jet_n);
    // dynamical castoting to pointers, null if not possible
    const auto * pf_jet = dynamic_cast<const reco::PFJet *>(&jet);
    const auto * pat_jet = dynamic_cast<const pat::Jet *>(&jet);
    edm::RefToBase<reco::Jet> jet_ref(jets, jet_n);
    // TagInfoCollection not in an associative container so search for matchs
    const edm::View<reco::ShallowTagInfo> & taginfos = *shallow_tag_infos;
    edm::Ptr<reco::ShallowTagInfo> match;
    // Try first by 'same index'
    if ((jet_n < taginfos.size()) && (taginfos[jet_n].jet() == jet_ref)) {
        match = taginfos.ptrAt(jet_n);
    } else {
      // otherwise fail back to a simple search
      for (auto itTI = taginfos.begin(), edTI = taginfos.end(); itTI != edTI; ++itTI) {
        if (itTI->jet() == jet_ref) { match = taginfos.ptrAt( itTI - taginfos.begin() ); break; }
      }
    }
    reco::ShallowTagInfo tag_info;
    if (match.isNonnull()) {
      tag_info = *match; 
    } // will be default values otherwise

    // fill basic jet features
    deep::jet_features_converter(jet, features.jet_features);

    // fill number of pv
    features.npv = vtxs->size();

    // fill features from ShallowTagInfo
    const auto & tag_info_vars = tag_info.taggingVariables();
    btag_features_converter(tag_info_vars, features.tag_info_features);

    // copy which will be sorted
    auto svs_sorted = *svs;     
    // sort by dxy
    std::sort(svs_sorted.begin(), svs_sorted.end(),
              [&pv](const auto & sva, const auto &svb)
              { return deep::sv_vertex_comparator(sva, svb, pv); });
    // fill features from secondary vertices
    for (const auto & sv : svs_sorted) {
      if (reco::deltaR(sv, jet) > jet_radius_) continue;
      else {
        features.sv_features.emplace_back();
        // in C++17 could just get from emplace_back output
        auto & sv_features = features.sv_features.back();
        deep::sv_features_converter(sv, pv, jet, sv_features);
      }
    }

    // stuff required for dealing with pf candidates 
    math::XYZVector jet_dir = jet.momentum().Unit();
    GlobalVector jet_ref_track_dir(jet.px(),
                                   jet.py(),
                                   jet.pz());

    std::vector<sorting::sortingClass<size_t> > c_sorted, n_sorted;

    deep::TrackInfoBuilder trackinfo(track_builder);

    // unsorted reference to sv
    const auto & svs_unsorted = *svs;     
    // fill collection, from DeepTNtuples plus some styling
    for (unsigned int i = 0; i <  jet.numberOfDaughters(); i++){
        auto cand = dynamic_cast<const reco::Candidate *>(jet.daughter(i));
        if(cand){
          if (cand->charge() != 0) {
            trackinfo.buildTrackInfo(cand,jet_dir,jet_ref_track_dir,pv);
            c_sorted.emplace_back(i, trackinfo.getTrackSip2dSig(),
                    -deep::mindrsvpfcand(svs_unsorted,cand), cand->pt()/jet.pt());
          } else {
            n_sorted.emplace_back(i, -1,
                    -deep::mindrsvpfcand(svs_unsorted,cand), cand->pt()/jet.pt());
          }
        }
    }

    // sort collections (open the black-box if you please) 
    std::sort(c_sorted.begin(),c_sorted.end(),
      sorting::sortingClass<std::size_t>::compareByABCInv);
    std::sort(n_sorted.begin(),n_sorted.end(),
      sorting::sortingClass<std::size_t>::compareByABCInv);

    std::vector<size_t> c_sortedindices,n_sortedindices;
   
    // this puts 0 everywhere and the right position in ind 
    c_sortedindices=sorting::invertSortingVector(c_sorted);
    n_sortedindices=sorting::invertSortingVector(n_sorted);

    // set right size to vectors
    features.c_pf_features.clear();
    features.c_pf_features.resize(c_sorted.size());
    features.n_pf_features.clear();
    features.n_pf_features.resize(n_sorted.size());



  for (unsigned int i = 0; i <  jet.numberOfDaughters(); i++){

    // get pointer and check that is correct
    auto cand = dynamic_cast<const reco::Candidate *>(jet.daughter(i));
    if(!cand) continue;
    auto packed_cand = dynamic_cast<const pat::PackedCandidate *>(cand);
    auto reco_cand = dynamic_cast<const reco::PFCandidate *>(cand);

    float drminpfcandsv = deep::mindrsvpfcand(svs_unsorted, cand);
    
    if (cand->charge() != 0) {
      // is charged candidate
      auto entry = c_sortedindices.at(i);
      // build track info
      trackinfo.buildTrackInfo(cand,jet_dir,jet_ref_track_dir,pv);
      // get_ref to vector element
      auto & c_pf_features = features.c_pf_features.at(entry);
      // fill feature structure 
      if (packed_cand) {
        deep::c_pf_packed_features_converter(packed_cand, jet, trackinfo, 
                                             drminpfcandsv, c_pf_features);
      } else if (reco_cand) {
        if (pf_jet) { 
        // need some edm::Ptr or edm::Ref
        auto reco_ptr = pf_jet->getPFConstituent(i);
        // get PUPPI weight from value map
        float puppiw = (*puppi_value_map)[reco_ptr];
        int pv_ass_quality = (*pvasq_value_map)[reco_ptr];
        deep::c_pf_reco_features_converter(reco_cand, jet, trackinfo, 
                                           drminpfcandsv, puppiw,
                                           pv_ass_quality, c_pf_features);
        }
      }
    } else {
      // is neutral candidate
      auto entry = n_sortedindices.at(i);
      // get_ref to vector element
      auto & n_pf_features = features.n_pf_features.at(entry);
      // fill feature structure 
      if (packed_cand) {
        deep::n_pf_packed_features_converter(packed_cand, jet, drminpfcandsv, 
                                            n_pf_features);
      } else if (reco_cand) {
        if (pf_jet) { 
        // need some edm::Ptr or edm::Ref
        auto reco_ptr = pf_jet->getPFConstituent(i);
        // get PUPPI weight from value map
        float puppiw = (*puppi_value_map)[reco_ptr];
        deep::n_pf_reco_features_converter(reco_cand, jet,
                                           drminpfcandsv, puppiw,
                                           n_pf_features);
        }
      }
    }

    
  }

    

  output_tag_infos->emplace_back(features, jet_ref);
  }

  iEvent.put(std::move(output_tag_infos));

}

//define this as a plug-in
DEFINE_FWK_MODULE(DeepFlavourTagInfoProducer);
