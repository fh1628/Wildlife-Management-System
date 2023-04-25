import APIService from "./APIService";


class ResearcherService extends APIService {
    getAllResearchers() {
        return this.get('/get_researchers')
    }
    addResearcher(arr: any[]) {
        const data = {
            Name: arr[0],
            Email: arr[1],
            Phone: arr[2],
            Expertise: arr[3],
            SpeciesScientificName: arr[4],
            PopulationID: arr[5],
        }
        return this.post('/add_researcher', data)
    }
    updateResearcher(arr: any) {
        const data = {
            Name: arr[0],
            Email: arr[1],
            Phone: arr[2],
            Expertise: arr[3],
            SpeciesScientificName: arr[4],
            PopulationID: arr[5],
        }
        console.log("NEW DATA", data)
        return this.put('/update_researcher', data)
    }
    deleteResearcher(arr: any) {
        const data = {
            Email: arr[1]
        }
        return this.delete('/del_researcher', data)
    }
    getFilteredResearchers(data: any) {
        return this.get('/get_researchers_filtered', data)
    }
    getColumn(params: any) {
        return this.get('/get_researcher_column', params);
    }
}

export default new ResearcherService();