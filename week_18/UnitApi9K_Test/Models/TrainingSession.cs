using System.ComponentModel.DataAnnotations;
using UnitApi9K.Enums;

namespace UnitApi9K.Models
{
    public class TrainingSession
    {
        public int Id { get; set; }
        public int DogId { get; set; }
        public Dog Dog { get; set; } = null!;

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

        public bool Passed { get; set; }

        [Required]
        [MaxLength(100)]
        public string Evaluator { get; set; } = string.Empty;
    }
}
