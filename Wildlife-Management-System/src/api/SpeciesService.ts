import APIService from "./APIService";


class SpeciesService extends APIService {
    getAllSpecies() {
        return this.get('/get_species')
    }
}

export default new SpeciesService();