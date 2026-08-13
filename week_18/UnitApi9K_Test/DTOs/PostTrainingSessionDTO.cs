using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class PostTrainingSessionDTO
{
    public int DogId { get; set; }
    public DateTime SessionDate { get; set; }
    public int DurationMinutes { get; set; }
    public TrainingTypes TrainingType { get; set; }
    public int PerformanceScore { get; set; }
    public string Evaluator { get; set; } = string.Empty;
}
