using Microsoft.AspNetCore.Mvc;
using UnitApi9K.DTOs;
using UnitApi9K.Enums;
using UnitApi9K.Models;
using UnitApi9K.Repositories;

namespace UnitApi9K.Controllers;


[ApiController]
[Route("api/dogs")]
public class DogsController : ControllerBase
{
    private readonly IUnitRepository _repo;

    public DogsController(IUnitRepository repo)
    {
        _repo = repo;
    }


    // Create new dog
    [HttpPost]
    public async Task<ActionResult<GetDogDTO>> CreateDogAsync(PostDogDTO dog)
    {
        // Validate whether is a future date
        if (dog.DateOfBirth.Date >= DateTime.Today)
        {
            return BadRequest("Unable to create an object with future date.");
        }

        var created = await _repo.CreateDogAsync(dog);

        return CreatedAtAction(
            nameof(GetDogById),
            new { id = created.Id },
            created);
    }


    // Get dog by id
    [HttpGet("{id}")]
    public async Task<IActionResult> GetDogById(int id)
    {
        var dog = await _repo.GetDogByIdAsync(id);
        if (dog == null)
        {
            return NotFound();
        }

        return Ok(dog);
    }


    // Get all dogs, filter by paramters
    [HttpGet("search")]
    public async Task<ActionResult<IEnumerable<FilterdDogDTO>>> Search(
        SpecialtyTypes? specialty, StatusTypes? status)
    {
        return Ok(await _repo.SearchAsync(specialty, status));
    }


    // Get dogs with handlers
    [HttpGet("with-handler")]
    public async Task<ActionResult<IEnumerable<DogWithHanlerDTO>>> GetDogsWithHandlers()
    {
        return Ok(await _repo.GetDogsWithHandlersAsync());
    }


    // Get summery performance
    [HttpGet("performance-summery")]
    public async Task<ActionResult<IEnumerable<SummeryPerformanceDTO>>>
        GetSummeryPerformance()
    {
        return Ok(await _repo.GetSummeryPerformanceAsync());
    }
}
