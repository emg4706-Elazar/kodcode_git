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

    [Required]
    public DateTime DateOfBirth { get; set; }

    [Required]
    public SpecialtyTypes Specialty { get; set; }

    public StatusTypes Status { get; set; } = StatusTypes.InTraining;
}
