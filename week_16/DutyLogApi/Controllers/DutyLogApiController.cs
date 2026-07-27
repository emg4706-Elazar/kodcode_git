using Microsoft.AspNetCore.Mvc;
using DutyLogApi.Models;

namespace DutyLogApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class DutyLogApiController : ControllerBase
{
    private static readonly List<DutyLog> _dutyLogs = new()
    {
        new DutyLog
        {
            Id = 1,
            Name = "John Doe",
            Station = 101,
            ShiftStart = new DateTime(2026, 6, 1, 08, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 1, 16, 00, 00),
            Remarks = "Morning shift, regular patrol."
        },

        new DutyLog
        {
            Id = 2,
            Name = "Jane Smith",
            Station = 102,
            ShiftStart = new DateTime(2026, 6, 2, 16, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 3, 00, 00, 00),
            Remarks = "Evening shift, handover completed smoothly."
        },
        new DutyLog
        {
            Id = 3,
            Name = "Michael Johnson",
            Station = 103,
            ShiftStart = new DateTime(2026, 6, 3, 00, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 3, 08, 00, 00),
            Remarks = "Night shift, quiet with no incidents."
        },
        new DutyLog
        {
            Id = 4,
            Name = "Emily Davis",
            Station = 101,
            ShiftStart = new DateTime(2026, 6, 4, 08, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 4, 16, 00, 00),
            Remarks = "Covering for team lead."
        },
        new DutyLog
        {
            Id = 5,
            Name = "David Brown",
            Station = 104,
            ShiftStart = new DateTime(2026, 6, 5, 12, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 5, 20, 00, 00),
            Remarks = "Mid-day shift at main station."
        },
        new DutyLog
        {
            Id = 6,
            Name = "Sarah Wilson",
            Station = 102,
            ShiftStart = new DateTime(2026, 6, 6, 08, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 6, 16, 00, 00),
            Remarks = "Routine equipment checks performed."
        },
        new DutyLog
        {
            Id = 7,
            Name = "James Taylor",
            Station = 105,
            ShiftStart = new DateTime(2026, 6, 7, 16, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 8, 00, 00, 00),
            Remarks = "Heavy traffic reported in the area."
        },
        new DutyLog
        {
            Id = 8,
            Name = "Jessica Anderson",
            Station = 103,
            ShiftStart = new DateTime(2026, 6, 8, 00, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 8, 08, 00, 00),
            Remarks = "System maintenance during the shift."
        },
        new DutyLog
        {
            Id = 9,
            Name = "Daniel Thomas",
            Station = 101,
            ShiftStart = new DateTime(2026, 6, 9, 08, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 9, 16, 00, 00),
            Remarks = "Training new personnel."
        },
        new DutyLog
        {
            Id = 10,
            Name = "Laura Martinez",
            Station = 104,
            ShiftStart = new DateTime(2026, 6, 10, 16, 00, 00),
            ShiftEnd = new DateTime(2026, 6, 11, 00, 00, 00),
            Remarks = "End of week review completed."
        }
    };

    private int _nextId = 11;

    [HttpGet]
    public ActionResult<List<DutyLog>> GetAllLogs()
    {
        return Ok(_dutyLogs);
    }

    [HttpGet("{id}")]
    public ActionResult<DutyLog> GetLogById(int id)
    {
        var log = _dutyLogs.Where(l => l.Id == id);

        if (log == null)
        {
            return NotFound();
        }

        return Ok(log);
    }

    [HttpPost]
    public ActionResult<DutyLog> CreateDutyLog(DutyLog log)
    {
        // Assign a new id
        log.Id = _nextId++;

        // Add to the list
        _dutyLogs.Add(log);

        return CreatedAtAction(
            nameof(GetLogById),
            new { id = log.Id },
            log);
    }

    [HttpPut("{id}")]
    public IActionResult UpdateLog(int id, DutyLog updatedLog)
    {
        var existingLog = _dutyLogs.FirstOrDefault(l => l.Id == id);

        if (existingLog == null)
        {
            return NotFound();
        }

        existingLog.Name = updatedLog.Name;
        existingLog.Station = updatedLog.Station;
        existingLog.ShiftStart = updatedLog.ShiftStart;
        existingLog.ShiftEnd = updatedLog.ShiftEnd;
        existingLog.Remarks = updatedLog.Remarks;

        return NoContent();
    }

    [HttpDelete("{id}")]
    public IActionResult DeleteLog(int id)
    {
        var log = _dutyLogs.FirstOrDefault(l => l.Id == id);

        if (log == null)
        {
            return NotFound();
        }

        _dutyLogs.Remove(log);

        return NoContent();
    }
}