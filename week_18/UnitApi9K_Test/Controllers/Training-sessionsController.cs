using Microsoft.AspNetCore.Mvc;
using UnitApi9K.DTOs;
using UnitApi9K.Enums;
using UnitApi9K.Models;
using UnitApi9K.Repositories;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Http.HttpResults;


namespace UnitApi9K.Controllers;

[ApiController]
[Route("api/training-sessions")]
public class TrainingSessionsController : ControllerBase
{
    private readonly IUnitRepository _repo;

    public TrainingSessionsController(IUnitRepository repo)
    {
        _repo = repo;
    }

    // Create new training session
    [HttpPost]
    public async Task<ActionResult<TrainingSession>> CreateTraining(PostTrainingSessionDTO training)
    {
        // Validate whether is a future date
        if (training.SessionDate.Date > DateTime.Today)
        {
            return BadRequest("Unable to assign a future date");
        }

        var dog = await _repo.GetDogByIdAsync(training.DogId);
        if (dog == null)
        {
            return NotFound($"The dog {training.DogId} not found.");
        }

        if (dog.Status == StatusTypes.Retired)
        {
            return BadRequest("Cannot create session training for retired dog.");
        }

        var created = await _repo.CreateTrainingAsync(training);

        return CreatedAtAction(
            nameof(GetTrainigSessionsDetailes),
            new { id = created.Id },
            created
            );
    }

    // Get all training sessions with detailes
    [HttpGet("detailed")]
    public async Task<ActionResult<IEnumerable<TrainingDetailesDTO>>>
        GetTrainigSessionsDetailes()
    {
        return Ok(await _repo.GetTrainigSessionsDetailesAsync());
    }

    // Get Paged of training sessions
    [HttpGet("paged")]
    public async Task<ActionResult<SessionsPagedDTO<SessionDTO>>>
        GetPaged(int page=1, [Range(5, 50)] int pageSize=10)
    {
        if (page < 1)
        {
            return BadRequest("Page nust be more then 0.");
        }

        return Ok(await _repo.GetPagedAsync(page, pageSize));
    }
}
