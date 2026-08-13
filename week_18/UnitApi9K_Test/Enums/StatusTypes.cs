using System.Text.Json.Serialization;

namespace UnitApi9K.Enums
{

    [JsonConverter(typeof(JsonStringEnumConverter))]
    public enum StatusTypes
    {
        Active,
        InTraining,
        Retired
    }
}
