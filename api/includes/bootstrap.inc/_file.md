# includes/bootstrap.inc

- **Source:** [local](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · 4082 lines

## File documentation

```text
@file
Functions that need to be loaded on every Drupal request.
```

## Functions (derived index)

- [timer_start()](timer_start.md) — Starts the timer with the specified name.
- [timer_read()](timer_read.md) — Reads the current timer value without stopping the timer.
- [timer_stop()](timer_stop.md) — Stops the timer with the specified name.
- [conf_path()](conf_path.md) — Returns the appropriate configuration directory.
- [drupal_override_server_variables()](drupal_override_server_variables.md) — Sets appropriate server variables needed for command line scripts to work.
- [drupal_environment_initialize()](drupal_environment_initialize.md) — Initializes the PHP environment.
- [drupal_valid_http_host()](drupal_valid_http_host.md) — Validates that a hostname (for example $_SERVER['HTTP_HOST']) is safe.
- [drupal_is_https()](drupal_is_https.md) — Checks whether an HTTPS request is being served.
- [drupal_settings_initialize()](drupal_settings_initialize.md) — Sets the base URL, cookie domain, and session name from configuration.
- [_drupal_get_cookie_domain()](_drupal_get_cookie_domain.md) — Derive the cookie domain to use for session cookies.
- [drupal_get_filename()](drupal_get_filename.md) — Returns and optionally sets the filename for a system resource.
- [_drupal_get_filename_fallback()](_drupal_get_filename_fallback.md) — Performs a cached file system scan as a fallback when searching for a file.
- [_drupal_file_scan_cache()](_drupal_file_scan_cache.md) — Returns the current list of cached file system scan results.
- [_drupal_get_filename_perform_file_scan()](_drupal_get_filename_perform_file_scan.md) — Performs a file system scan to search for a system resource.
- [_drupal_get_filename_fallback_trigger_error()](_drupal_get_filename_fallback_trigger_error.md) — Triggers a user-level warning for missing or unexpectedly moved files.
- [_drupal_trigger_error_with_delayed_logging()](_drupal_trigger_error_with_delayed_logging.md) — Invokes trigger_error() with logging delayed until the end of the request.
- [drupal_trigger_fatal_error()](drupal_trigger_fatal_error.md) — Invoke trigger_error() using a fatal error that will terminate the request.
- [drupal_file_scan_write_cache()](drupal_file_scan_write_cache.md) — Writes the file scan cache to the persistent cache.
- [variable_initialize()](variable_initialize.md) — Loads the persistent variable table.
- [variable_get()](variable_get.md) — Returns a persistent variable.
- [variable_set()](variable_set.md) — Sets a persistent variable.
- [variable_del()](variable_del.md) — Unsets a persistent variable.
- [drupal_page_get_cache()](drupal_page_get_cache.md) — Retrieves the current page from the cache.
- [drupal_page_is_cacheable()](drupal_page_is_cacheable.md) — Determines the cacheability of the current page.
- [bootstrap_invoke_all()](bootstrap_invoke_all.md) — Invokes a bootstrap hook in all bootstrap modules that implement it.
- [drupal_load()](drupal_load.md) — Includes a file with the provided type and name.
- [drupal_add_http_header()](drupal_add_http_header.md) — Sets an HTTP response header for the current page.
- [drupal_get_http_header()](drupal_get_http_header.md) — Gets the HTTP response headers for the current page.
- [_drupal_set_preferred_header_name()](_drupal_set_preferred_header_name.md) — Sets the preferred name for the HTTP header.
- [drupal_send_headers()](drupal_send_headers.md) — Sends the HTTP response headers that were previously set, adding defaults.
- [drupal_page_header()](drupal_page_header.md) — Sets HTTP headers in preparation for a page response.
- [drupal_serve_page_from_cache()](drupal_serve_page_from_cache.md) — Sets HTTP headers in preparation for a cached page response.
- [bootstrap_hooks()](bootstrap_hooks.md) — Defines the critical hooks that force modules to always be loaded.
- [drupal_unpack()](drupal_unpack.md) — Unserializes and appends elements from a serialized string.
- [t()](t.md) — Translates a string to the current language or to a given language.
- [format_string()](format_string.md) — Formats a string for HTML display by replacing variable placeholders.
- [check_plain()](check_plain.md) — Encodes special characters in a plain-text string for display as HTML.
- [drupal_validate_utf8()](drupal_validate_utf8.md) — Checks whether a string is valid UTF-8.
- [request_uri()](request_uri.md) — Returns the equivalent of Apache's $_SERVER['REQUEST_URI'] variable.
- [watchdog_exception()](watchdog_exception.md) — Logs an exception.
- [watchdog()](watchdog.md) — Logs a system message.
- [drupal_set_message()](drupal_set_message.md) — Sets a message to display to the user.
- [drupal_get_messages()](drupal_get_messages.md) — Returns all messages that have been set with drupal_set_message().
- [drupal_get_title()](drupal_get_title.md) — Gets the title of the current page.
- [drupal_set_title()](drupal_set_title.md) — Sets the title of the current page.
- [drupal_is_denied()](drupal_is_denied.md) — Checks to see if an IP address has been blocked.
- [drupal_block_denied()](drupal_block_denied.md) — Handles denied users.
- [drupal_random_key()](drupal_random_key.md) — Returns a URL-safe, base64 encoded string of highly randomized bytes (over the full 8-bit range).
- [drupal_base64_encode()](drupal_base64_encode.md) — Returns a URL-safe, base64 encoded version of the supplied string.
- [drupal_random_bytes()](drupal_random_bytes.md) — Returns a string of highly randomized bytes (over the full 8-bit range).
- [drupal_hmac_base64()](drupal_hmac_base64.md) — Calculates a base-64 encoded, URL-safe sha-256 hmac.
- [drupal_hash_base64()](drupal_hash_base64.md) — Calculates a base-64 encoded, URL-safe sha-256 hash.
- [drupal_array_merge_deep()](drupal_array_merge_deep.md) — Merges multiple arrays, recursively, and returns the merged array.
- [drupal_array_merge_deep_array()](drupal_array_merge_deep_array.md) — Merges multiple arrays, recursively, and returns the merged array.
- [drupal_anonymous_user()](drupal_anonymous_user.md) — Generates a default anonymous $user object.
- [drupal_bootstrap()](drupal_bootstrap.md) — Ensures Drupal is bootstrapped to the specified phase.
- [drupal_get_user_timezone()](drupal_get_user_timezone.md) — Returns the time zone of the current user.
- [drupal_get_hash_salt()](drupal_get_hash_salt.md) — Gets a salt useful for hardening against SQL injection.
- [_drupal_error_handler()](_drupal_error_handler.md) — Provides custom PHP error handling.
- [_drupal_exception_handler()](_drupal_exception_handler.md) — Provides custom PHP exception handling.
- [_drupal_bootstrap_configuration()](_drupal_bootstrap_configuration.md) — Sets up the script environment and loads settings.php.
- [_drupal_bootstrap_page_cache()](_drupal_bootstrap_page_cache.md) — Attempts to serve a page from the cache.
- [_drupal_bootstrap_database()](_drupal_bootstrap_database.md) — Initializes the database system and registers autoload functions.
- [_drupal_bootstrap_variables()](_drupal_bootstrap_variables.md) — Loads system variables and all enabled bootstrap modules.
- [_drupal_bootstrap_page_header()](_drupal_bootstrap_page_header.md) — Invokes hook_boot(), initializes locking system, and sends HTTP headers.
- [drupal_get_bootstrap_phase()](drupal_get_bootstrap_phase.md) — Returns the current bootstrap phase for this Drupal process.
- [drupal_valid_test_ua()](drupal_valid_test_ua.md) — Returns the test prefix if this is an internal request from SimpleTest.
- [drupal_generate_test_ua()](drupal_generate_test_ua.md) — Generates a user agent string with a HMAC and timestamp for simpletest.
- [drupal_maintenance_theme()](drupal_maintenance_theme.md) — Enables use of the theme system without requiring database access.
- [drupal_fast_404()](drupal_fast_404.md) — Returns a simple 404 Not Found page.
- [drupal_installation_attempted()](drupal_installation_attempted.md) — Returns TRUE if a Drupal installation is currently being attempted.
- [get_t()](get_t.md) — Returns the name of the proper localization function.
- [drupal_language_initialize()](drupal_language_initialize.md) — Initializes all the defined language types.
- [drupal_language_types()](drupal_language_types.md) — Returns a list of the built-in language types.
- [drupal_multilingual()](drupal_multilingual.md) — Returns TRUE if there is more than one language enabled.
- [language_types()](language_types.md) — Returns an array of the available language types.
- [language_list()](language_list.md) — Returns a list of installed languages, indexed by the specified key.
- [language_default()](language_default.md) — Returns the default language, as an object, or one of its properties.
- [request_path()](request_path.md) — Returns the requested URL path of the page being viewed.
- [arg()](arg.md) — Returns a component of the current Drupal path.
- [ip_address()](ip_address.md) — Returns the IP address of the client machine.
- [drupal_get_schema()](drupal_get_schema.md) — Gets the schema definition of a table, or the whole database schema.
- [drupal_get_complete_schema()](drupal_get_complete_schema.md) — Gets the whole database schema.
- [drupal_autoload_interface()](drupal_autoload_interface.md) — Confirms that an interface is available.
- [drupal_autoload_class()](drupal_autoload_class.md) — Confirms that a class is available.
- [drupal_autoload_trait()](drupal_autoload_trait.md) — Confirms that a trait is available.
- [_registry_check_code()](_registry_check_code.md) — Checks for a resource in the registry.
- [registry_rebuild()](registry_rebuild.md) — Rescans all enabled modules and rebuilds the registry.
- [registry_update()](registry_update.md) — Updates the registry based on the latest files listed in the database.
- [drupal_static()](drupal_static.md) — Provides central static variable storage.
- [drupal_static_reset()](drupal_static_reset.md) — Resets one or all centrally stored static variable(s).
- [drupal_is_cli()](drupal_is_cli.md) — Detects whether the current script is running in a command-line environment.
- [drupal_placeholder()](drupal_placeholder.md) — Formats text for emphasized display in a placeholder inside a sentence.
- [drupal_register_shutdown_function()](drupal_register_shutdown_function.md) — Registers a function for execution on shutdown.
- [_drupal_shutdown_function()](_drupal_shutdown_function.md) — Executes registered shutdown functions.
- [drupal_check_memory_limit()](drupal_check_memory_limit.md) — Compares the memory required for an operation to the available memory.
- [drupal_clear_opcode_cache()](drupal_clear_opcode_cache.md) — Invalidates a PHP file from any active opcode caches.
- [drupal_check_trusted_hosts()](drupal_check_trusted_hosts.md) — Checks trusted HTTP Host headers to protect against header injection attacks.
- [drupal_setcookie()](drupal_setcookie.md) — Drupal's wrapper around PHP's setcookie() function.
- [_drupal_cookie_params()](_drupal_cookie_params.md) — Process the params for cookies. This emulates support for the SameSite attribute in earlier versions of PHP, and allows the value of that attribute to be overridden.
- [_drupal_samesite_cookie()](_drupal_samesite_cookie.md) — Determine the value for the samesite cookie attribute, in the following order of precedence:

## Classes and interfaces (derived index)

- [DrupalCacheArray](DrupalCacheArray.md) — Provides a caching wrapper to be used in place of large array structures.
- [SchemaCache](SchemaCache.md) — Extends DrupalCacheArray to allow for dynamic building of the schema cache.

## Constants

### VERSION

- Line 11

```php
define('VERSION', '7.103');
```

```text
The current system version.
```

### DRUPAL_CORE_COMPATIBILITY

- Line 16

```php
define('DRUPAL_CORE_COMPATIBILITY', '7.x');
```

```text
Core API compatibility.
```

### DRUPAL_MINIMUM_PHP

- Line 21

```php
define('DRUPAL_MINIMUM_PHP', '5.3.3');
```

```text
Minimum supported version of PHP.
```

### DRUPAL_MINIMUM_PHP_MEMORY_LIMIT

- Line 26

```php
define('DRUPAL_MINIMUM_PHP_MEMORY_LIMIT', '32M');
```

```text
Minimum recommended value of PHP memory_limit.
```

### ERROR_REPORTING_HIDE

- Line 31

```php
define('ERROR_REPORTING_HIDE', 0);
```

```text
Error reporting level: display no errors.
```

### ERROR_REPORTING_DISPLAY_SOME

- Line 36

```php
define('ERROR_REPORTING_DISPLAY_SOME', 1);
```

```text
Error reporting level: display errors and warnings.
```

### ERROR_REPORTING_DISPLAY_ALL

- Line 41

```php
define('ERROR_REPORTING_DISPLAY_ALL', 2);
```

```text
Error reporting level: display all messages.
```

### CACHE_PERMANENT

- Line 48

```php
define('CACHE_PERMANENT', 0);
```

```text
Indicates that the item should never be removed unless explicitly selected.

The item may be removed using cache_clear_all() with a cache ID.
```

### CACHE_TEMPORARY

- Line 53

```php
define('CACHE_TEMPORARY', -1);
```

```text
Indicates that the item should be removed at the next general cache wipe.
```

### WATCHDOG_EMERGENCY

- Line 78; topics: logging_severity_levels

```php
define('WATCHDOG_EMERGENCY', 0);
```

```text
Log message severity -- Emergency: system is unusable.
```

### WATCHDOG_ALERT

- Line 83; topics: logging_severity_levels

```php
define('WATCHDOG_ALERT', 1);
```

```text
Log message severity -- Alert: action must be taken immediately.
```

### WATCHDOG_CRITICAL

- Line 88; topics: logging_severity_levels

```php
define('WATCHDOG_CRITICAL', 2);
```

```text
Log message severity -- Critical conditions.
```

### WATCHDOG_ERROR

- Line 93; topics: logging_severity_levels

```php
define('WATCHDOG_ERROR', 3);
```

```text
Log message severity -- Error conditions.
```

### WATCHDOG_WARNING

- Line 98; topics: logging_severity_levels

```php
define('WATCHDOG_WARNING', 4);
```

```text
Log message severity -- Warning conditions.
```

### WATCHDOG_NOTICE

- Line 103; topics: logging_severity_levels

```php
define('WATCHDOG_NOTICE', 5);
```

```text
Log message severity -- Normal but significant conditions.
```

### WATCHDOG_INFO

- Line 108; topics: logging_severity_levels

```php
define('WATCHDOG_INFO', 6);
```

```text
Log message severity -- Informational messages.
```

### WATCHDOG_DEBUG

- Line 113; topics: logging_severity_levels

```php
define('WATCHDOG_DEBUG', 7);
```

```text
Log message severity -- Debug-level messages.
```

### DRUPAL_BOOTSTRAP_CONFIGURATION

- Line 122

```php
define('DRUPAL_BOOTSTRAP_CONFIGURATION', 0);
```

```text
First bootstrap phase: initialize configuration.
```

### DRUPAL_BOOTSTRAP_PAGE_CACHE

- Line 127

```php
define('DRUPAL_BOOTSTRAP_PAGE_CACHE', 1);
```

```text
Second bootstrap phase: try to serve a cached page.
```

### DRUPAL_BOOTSTRAP_DATABASE

- Line 132

```php
define('DRUPAL_BOOTSTRAP_DATABASE', 2);
```

```text
Third bootstrap phase: initialize database layer.
```

### DRUPAL_BOOTSTRAP_VARIABLES

- Line 137

```php
define('DRUPAL_BOOTSTRAP_VARIABLES', 3);
```

```text
Fourth bootstrap phase: initialize the variable system.
```

### DRUPAL_BOOTSTRAP_SESSION

- Line 142

```php
define('DRUPAL_BOOTSTRAP_SESSION', 4);
```

```text
Fifth bootstrap phase: initialize session handling.
```

### DRUPAL_BOOTSTRAP_PAGE_HEADER

- Line 147

```php
define('DRUPAL_BOOTSTRAP_PAGE_HEADER', 5);
```

```text
Sixth bootstrap phase: set up the page header.
```

### DRUPAL_BOOTSTRAP_LANGUAGE

- Line 152

```php
define('DRUPAL_BOOTSTRAP_LANGUAGE', 6);
```

```text
Seventh bootstrap phase: find out language of the page.
```

### DRUPAL_BOOTSTRAP_FULL

- Line 157

```php
define('DRUPAL_BOOTSTRAP_FULL', 7);
```

```text
Final bootstrap phase: Drupal is fully loaded; validate and fix input data.
```

### DRUPAL_ANONYMOUS_RID

- Line 162

```php
define('DRUPAL_ANONYMOUS_RID', 1);
```

```text
Role ID for anonymous users; should match what's in the "role" table.
```

### DRUPAL_AUTHENTICATED_RID

- Line 167

```php
define('DRUPAL_AUTHENTICATED_RID', 2);
```

```text
Role ID for authenticated users; should match what's in the "role" table.
```

### DRUPAL_KILOBYTE

- Line 174

```php
define('DRUPAL_KILOBYTE', 1024);
```

```text
The number of bytes in a kilobyte.

For more information, visit http://en.wikipedia.org/wiki/Kilobyte.
```

### LANGUAGE_NONE

- Line 181

```php
define('LANGUAGE_NONE', 'und');
```

```text
The language code used when no language is explicitly assigned.

Defined by ISO639-2 for "Undetermined".
```

### LANGUAGE_TYPE_CONTENT

- Line 186

```php
define('LANGUAGE_TYPE_CONTENT', 'language_content');
```

```text
The type of language used to define the content language.
```

### LANGUAGE_TYPE_INTERFACE

- Line 191

```php
define('LANGUAGE_TYPE_INTERFACE', 'language');
```

```text
The type of language used to select the user interface.
```

### LANGUAGE_TYPE_URL

- Line 196

```php
define('LANGUAGE_TYPE_URL', 'language_url');
```

```text
The type of language used for URLs.
```

### LANGUAGE_LTR

- Line 201

```php
define('LANGUAGE_LTR', 0);
```

```text
Language written left to right. Possible value of $language->direction.
```

### LANGUAGE_RTL

- Line 206

```php
define('LANGUAGE_RTL', 1);
```

```text
Language written right to left. Possible value of $language->direction.
```

### REQUEST_TIME

- Line 218

```php
define('REQUEST_TIME', (int) $_SERVER['REQUEST_TIME']);
```

```text
Time of the current request in seconds elapsed since the Unix Epoch.

This differs from $_SERVER['REQUEST_TIME'], which is stored as a float
since PHP 5.4.0. Float timestamps confuse most PHP functions
(including date_create()).

@see http://php.net/manual/reserved.variables.server.php
@see http://php.net/manual/function.time.php
```

### CHECK_PLAIN

- Line 225

```php
define('CHECK_PLAIN', 0);
```

```text
Flag used to indicate that text is not sanitized, so run check_plain().

@see drupal_set_title()
```

### PASS_THROUGH

- Line 232

```php
define('PASS_THROUGH', -1);
```

```text
Flag used to indicate that text has already been sanitized.

@see drupal_set_title()
```

### REGISTRY_RESET_LOOKUP_CACHE

- Line 237

```php
define('REGISTRY_RESET_LOOKUP_CACHE', 1);
```

```text
Signals that the registry lookup cache should be reset.
```

### REGISTRY_WRITE_LOOKUP_CACHE

- Line 242

```php
define('REGISTRY_WRITE_LOOKUP_CACHE', 2);
```

```text
Signals that the registry lookup cache should be written to storage.
```

### DRUPAL_PHP_FUNCTION_PATTERN

- Line 249

```php
define('DRUPAL_PHP_FUNCTION_PATTERN', '[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*');
```

```text
Regular expression to match PHP function names.

@see http://php.net/manual/language.functions.php
```

### DATE_RFC7231

- Line 262

```php
define('DATE_RFC7231', 'D, d M Y H:i:s \G\M\T');
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
