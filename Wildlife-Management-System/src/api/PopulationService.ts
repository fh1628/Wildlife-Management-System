import APIService from "./APIService";


class PopulationService extends APIService {
    getAllPopulations() {
        return this.get('/get_populations')
    }
}

export default new PopulationService();