import APIService from "./APIService";


class SpeciesService extends APIService {
    getAllSpecies() {
        return this.get('/get_species')
    }

    addSpecies(arr: any[]) {
        const data = {
            ScientificName: arr[0],
            CommonName: arr[1],
            ConservationStatus: arr[2],
            GeographicDistribution: arr[3],
        }
        return this.post('/add_species', data)
    }
    updateSpecies(arr: any) {
        const data = {
            ScientificName: arr[0],
            CommonName: arr[1],
            ConservationStatus: arr[2],
            GeographicDistribution: arr[3],
        }
        console.log("NEW DATA", data)
        return this.put('/update_species', data)
    }
    deleteSpecies(arr: any) {
        const data = {
            ScientificName: arr[0]
        }
        return this.delete('/del_species', data)
    }
    getFilteredSpecies(data: any) {
        return this.get('/get_species_filtered', data)
    }
    getColumn(params: any) {
        return this.get('/get_species_column', params);
    }
    getByPopulation(location: string) {
        return this.get('/get_species_in_location', {LocationName: location})
    }
}

export default new SpeciesService();
