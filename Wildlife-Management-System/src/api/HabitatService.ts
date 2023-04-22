import APIService from "./APIService";


class HabitatService extends APIService {
    getAllHabitats() {
        return this.get('/get_habitats')
    }
}

export default new HabitatService();