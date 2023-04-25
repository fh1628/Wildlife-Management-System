import APIService from "./APIService";


class HabitatService extends APIService {
    getFilteredHabitats(params: any) {
        return this.get('/get_habitats_filtered', params)
    }

    getColumn(params: any) {
        return this.get('/get_habitat_column', params);
    }

    addHabitat(arr: any[]) {
        const data = {
            HabitatName: arr[0],
            HabitatType: arr[1],
            ConservationStatus: arr[2],
            DegradationLevel: arr[3],
            Latitude: arr[4],
            Longitude: arr[5],
        }
        return this.post('/add_habitat', data)
    }
    updateHabitat(arr: any) {
        const data = {
            HabitatName: arr[0],
            HabitatType: arr[1],
            ConservationStatus: arr[2],
            DegradationLevel: arr[3],
            Latitude: arr[4],
            Longitude: arr[5],
        }
        return this.put('/update_habitat', data)
        }

    deleteHabitat(arr: any) {
        const data = {
            HabitatName: arr[0],
        }
        return this.delete('/del_habitat', data)
    }
    sort(params: any) {
        return this.get('sort_habitats_by_degradation', params)
    }
}

export default new HabitatService();
