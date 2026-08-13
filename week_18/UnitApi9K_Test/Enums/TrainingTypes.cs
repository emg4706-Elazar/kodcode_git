using System.Text.Json.Serialization;

namespace UnitApi9K.Enums
{
    [JsonConverter(typeof(JsonStringEnumConverter))]
    public enum TrainingTypes
    {
        Obedience,
        ScentDetection,
        Agility,
        FieldExercise,
        Endurance
    }
}
