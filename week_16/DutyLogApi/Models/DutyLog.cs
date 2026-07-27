using System.ComponentModel.DataAnnotations;

namespace DutyLogApi.Models
{
    public class DutyLog
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public int Station { get; set; }

        [Range(typeof(DateTime), "2026-01-01 00:00:00", "2030-12-31 23:59:59")]
        public DateTime ShiftStart { get; set; }

        [Range(typeof(DateTime), "2026-01-01 00:00:00", "2030-12-31 23:59:59")]
        public DateTime ShiftEnd { get; set; }

        [StringLength(500)]
        public string Remarks { get; set; }
    }
}
