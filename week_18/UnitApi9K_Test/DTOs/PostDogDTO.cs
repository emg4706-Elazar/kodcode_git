using System.ComponentModel.DataAnnotations;
using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class PostDogDTO
{
    [Required]
    [MaxLength(50)]
    public string Name { get; set; } = string.Empty;

    [Required]
    [MaxLength(50)]
    public string Breed { get; set; } = string.Empty;

    [Required]
    [MaxLength(15)]
    public string MicrochipId { get; set; } = string.Empty;

    public required DateTime DateOfBirth { get; set; }

    public required SpecialtyTypes Specialty { get; set; }

    public required StatusTypes Status { get; set; } = StatusTypes.InTraining;
}
