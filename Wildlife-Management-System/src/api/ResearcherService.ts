import APIService from "./APIService";


class ResearcherService extends APIService {
    getAllResearchers() {
        return this.get('/get_researchers')
    }
}

export default new ResearcherService();