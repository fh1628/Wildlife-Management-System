import APIService from "./APIService";


class OrganizationService extends APIService {
    getAllOrganizations() {
        return this.get('/get_organizations')
    }
}

export default new OrganizationService();