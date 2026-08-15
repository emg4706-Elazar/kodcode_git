using UnitApi9K.Enums;
using System.ComponentModel.DataAnnotations;


namespace UnitApi9K.DTOs;

public class PostTrainingSessionDTO
{
    public required int DogId { get; set; }

    public required DateTime SessionDate { get; set; }

    [Range(1, 300)]
    public required int DurationMinutes { get; set; }

    public required TrainingTypes TrainingType { get; set; }

    [Range(0, 100)]
    public required int PerformanceScore { get; set; }

    [Required]
    [MaxLength(100)]
    public string Evaluator { get; set; } = string.Empty;
}
