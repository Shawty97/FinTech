using RestSharp;

// Erstelle ein neues RestSharp-Client-Objekt
var client = new RestClient("https://example.com/webhook");

// Erstelle ein neues Request-Objekt
var request = new RestRequest(Method.POST);

// Füge den JSON-Body hinzu
request.AddJsonBody(new { message = "Hallo, Welt!" });

// Sende die Anfrage
var response = client.Execute(request);

// Überprüfe den Statuscode
if (response.StatusCode == System.Net.HttpStatusCode.OK)
{
    Console.WriteLine("Webhook erfolgreich gesendet!");
}