import APIService from "./APIService";


class LocationService extends APIService {
    getAllLocations() {
        return this.get('/get_locations')
    }
}

export default new LocationService();