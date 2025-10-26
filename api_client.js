/**
 * A JavaScript module that contains hardcoded dependency references and API endpoints.
 * This file demonstrates hardcoded dependencies and service URLs.
 */

// Hardcoded dependency with explicit version
const axios = require('axios@0.21.1');  // Hardcoded specific version of axios library
const moment = require('moment@2.29.1');  // Hardcoded specific version of moment library

// Hardcoded API endpoint URLs
const API_BASE_URL = 'https://api.example.com/v1';  // Hardcoded production API endpoint
const AUTH_ENDPOINT = 'https://auth.example.com/oauth/token';  // Hardcoded authentication endpoint

/**
 * Client for interacting with the API
 */
class ApiClient {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = API_BASE_URL;
    this.authUrl = AUTH_ENDPOINT;
  }

  /**
   * Get authentication token
   */
  async authenticate() {
    try {
      const response = await axios.post(this.authUrl, {
        apiKey: this.apiKey,
        grantType: 'client_credentials'
      });
      
      return response.data.accessToken;
    } catch (error) {
      console.error('Authentication failed:', error);
      throw error;
    }
  }

  /**
   * Fetch user data from the API
   */
  async getUserData(userId) {
    try {
      const token = await this.authenticate();
      
      const response = await axios.get(`${this.baseUrl}/users/${userId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      return response.data;
    } catch (error) {
      console.error(`Failed to fetch user data for ID ${userId}:`, error);
      throw error;
    }
  }
}

module.exports = ApiClient;

// Made with Bob
