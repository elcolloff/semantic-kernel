def test_dummy(): pass    # three registrations without factories
    expected_actor_types = {ProcessActor, StepActor, EventBufferActor, MessageBufferActor, ExternalEventBufferActor}
    registered_actor_types = {reg["actor_type"] for reg in mock_actor.registrations}

    assert expected_actor_types == registered_actor_types

    # Verify that ProcessActor and StepActor registrations have an actor_factory
    for reg in mock_actor.registrations:
        if reg["actor_type"] in {ProcessActor, StepActor}:
            assert reg["actor_factory"] is not None
        else:
            assert reg.get("actor_factory") is None


def test_register_flask_dapr_actors(mock_kernel, mock_factories):
    """Test that register_flask_dapr_actors registers all the required actors with appropriate factories for Flask."""
    mock_actor = MockFlaskDaprActor()

    # Call the synchronous registration function
    register_flask_dapr_actors(mock_actor, mock_kernel, mock_factories)

    # There should be 5 registrations: ProcessActor, StepActor (with factories) and
    # three registrations without factories
    expected_actor_types = {ProcessActor, StepActor, EventBufferActor, MessageBufferActor, ExternalEventBufferActor}
    registered_actor_types = {reg["actor_type"] for reg in mock_actor.registrations}

    assert expected_actor_types == registered_actor_types

    # Check that ProcessActor and StepActor registrations have non-null actor_factory
    for reg in mock_actor.registrations:
        if reg["actor_type"] in {ProcessActor, StepActor}:
            assert reg["actor_factory"] is not None
        else:
            assert reg.get("actor_factory") is None
