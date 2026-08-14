using UnitApi9K.Enums;
using System.ComponentModel.DataAnnotations;


namespace UnitApi9K.DTOs;

public class PostTrainingSessionDTO
{
    [Required]
    public int DogId { get; set; }

    [Required]
    public DateTime SessionDate { get; set; }

    [Required]
    [Range(1, 300)]
    public int DurationMinutes { get; set; }

    [Required]
    public TrainingTypes TrainingType { get; set; }

    [Required]
    [Range(0, 100)]
    public int PerformanceScore { get; set; }

    [Required]
    [MaxLength(100)]
    public string Evaluator { get; set; } = string.Empty;
}
