/*
 * OpenAPI Petstore
 *
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using Xunit;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;
using Org.OpenAPITools.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace Org.OpenAPITools.Test.Others
{
    /// <summary>
    ///  Class for testing Petstore
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class PetstoreTests : IDisposable
    {
        // TODO uncomment below to declare an instance variable for Cat
        //private Cat instance;

        public PetstoreTests()
        {
            // TODO uncomment below to create an instance of Cat
            //instance = new Cat();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of Cat
        /// </summary>
        [Fact]
        public void CatInstanceTest()
        {
            // test to ensure both Cat and Animal (parent) can have "AdditionalProperties", which result in warnings
            Cat c = JsonConvert.DeserializeObject<Cat>("{\"className\":\"cat\",\"bar\":\"from json bar\"}");
            Assert.Equal("from json bar", c.AdditionalProperties["bar"]);
        }

    }

}