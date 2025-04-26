# Logging Best Practices

## General Guidelines

1. **Use the right log level**
   - `DEBUG`: Detailed information, typically of interest only when diagnosing problems
   - `INFO`: Confirmation that things are working as expected
   - `WARNING`: Indication that something unexpected happened, but the application is still working
   - `ERROR`: Due to a more serious problem, the application has failed to perform a function
   - `CRITICAL`: A serious error, indicating that the application itself may be unable to continue running

2. **Structure your logs**
   - Always use structured logging format (key-value pairs)
   - Use snake_case for log keys
   - Log full objects only when necessary

3. **Include context**
   - Always include relevant identifiers (user_id, request_id, order_id, etc.)
   - Add business-relevant context (operation name, entity affected, result)

## Code Examples

### Good logging examples:

```python
# Good - structured, clear, with context
logger.info("User registration successful", user_id=user.id, email_verified=user.email_verified)

# Good - error with context
logger.error("Payment processing failed", 
             user_id=user.id, 
             payment_id=payment.id, 
             error_code=e.code)
```

### Bad logging examples:

```python
# Bad - unstructured, lacks context
logger.info("User registered")

# Bad - sensitive data exposure
logger.debug(f"User {user.email} entered password {password}")

# Bad - log message doesn't match level
logger.debug("CRITICAL DATABASE ERROR")
```

## Security Considerations

1. **Never log sensitive information**
   - Passwords, tokens, API keys
   - Full credit card numbers, social security numbers
   - Personal health information
   
2. **Log security events**
   - Authentication attempts (successful and failed)
   - Access control changes
   - Data exports
   
3. **Use the security logger for security-related events**
   ```python
   from core.utils.logging_utils import security_logger
   
   security_logger.info(
       "User role changed",
       user_id=user.id,
       old_role=old_role,
       new_role=new_role,
       changed_by=admin.id
   )
   ```

## Performance Logging

Use the performance logger and timing decorator for tracking execution times:

```python
from core.utils.logging_utils import performance_logger, log_timing

@log_timing
def expensive_operation():
    # Code here
    
# Or manually:
performance_logger.info(
    "Database query completed",
    query_name="find_active_users",
    duration_ms=duration,
    result_count=len(results)
)
```

## Best Practices for Log Messages

1. **Be specific and descriptive**
   - Good: "User password reset email sent"
   - Bad: "Email sent"
   
2. **Use consistent terminology**
   - Be consistent with event names and contexts across the application
   
3. **Include actionable information**
   - Include enough detail to troubleshoot issues
   - Consider what you'd need to know if investigating a problem
