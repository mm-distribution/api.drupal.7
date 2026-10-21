# drupal_bootstrap()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2553–2629 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2553-L2629)

## Signature

```php
function drupal_bootstrap($phase = NULL, $new_phase = TRUE)
```

## Documentation

```text
Ensures Drupal is bootstrapped to the specified phase.

In order to bootstrap Drupal from another PHP script, you can use this code:
@code
  define('DRUPAL_ROOT', '/path/to/drupal');
  require_once DRUPAL_ROOT . '/includes/bootstrap.inc';
  drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
@endcode

@param int $phase
  A constant telling which phase to bootstrap to. When you bootstrap to a
  particular phase, all earlier phases are run automatically. Possible
  values:
  - DRUPAL_BOOTSTRAP_CONFIGURATION: Initializes configuration.
  - DRUPAL_BOOTSTRAP_PAGE_CACHE: Tries to serve a cached page.
  - DRUPAL_BOOTSTRAP_DATABASE: Initializes the database layer.
  - DRUPAL_BOOTSTRAP_VARIABLES: Initializes the variable system.
  - DRUPAL_BOOTSTRAP_SESSION: Initializes session handling.
  - DRUPAL_BOOTSTRAP_PAGE_HEADER: Sets up the page header.
  - DRUPAL_BOOTSTRAP_LANGUAGE: Finds out the language of the page.
  - DRUPAL_BOOTSTRAP_FULL: Fully loads Drupal. Validates and fixes input
    data.
@param boolean $new_phase
  A boolean, set to FALSE if calling drupal_bootstrap from inside a
  function called from drupal_bootstrap (recursion).

@return int
  The most recently completed phase.
```

## Code

```php
function drupal_bootstrap($phase = NULL, $new_phase = TRUE) {
  // Not drupal_static(), because does not depend on any run-time information.
  static $phases = array(
    DRUPAL_BOOTSTRAP_CONFIGURATION,
    DRUPAL_BOOTSTRAP_PAGE_CACHE,
    DRUPAL_BOOTSTRAP_DATABASE,
    DRUPAL_BOOTSTRAP_VARIABLES,
    DRUPAL_BOOTSTRAP_SESSION,
    DRUPAL_BOOTSTRAP_PAGE_HEADER,
    DRUPAL_BOOTSTRAP_LANGUAGE,
    DRUPAL_BOOTSTRAP_FULL,
  );
  // Not drupal_static(), because the only legitimate API to control this is to
  // call drupal_bootstrap() with a new phase parameter.
  static $final_phase;
  // Not drupal_static(), because it's impossible to roll back to an earlier
  // bootstrap state.
  static $stored_phase = -1;

  if (isset($phase)) {
    // When not recursing, store the phase name so it's not forgotten while
    // recursing but take care of not going backwards.
    if ($new_phase && $phase >= $stored_phase) {
      $final_phase = $phase;
    }

    // Call a phase if it has not been called before and is below the requested
    // phase.
    while ($phases && $phase > $stored_phase && $final_phase > $stored_phase) {
      $current_phase = array_shift($phases);

      // This function is re-entrant. Only update the completed phase when the
      // current call actually resulted in a progress in the bootstrap process.
      if ($current_phase > $stored_phase) {
        $stored_phase = $current_phase;
      }

      switch ($current_phase) {
        case DRUPAL_BOOTSTRAP_CONFIGURATION:
          require_once DRUPAL_ROOT . '/includes/request-sanitizer.inc';
          _drupal_bootstrap_configuration();
          break;

        case DRUPAL_BOOTSTRAP_PAGE_CACHE:
          _drupal_bootstrap_page_cache();
          break;

        case DRUPAL_BOOTSTRAP_DATABASE:
          _drupal_bootstrap_database();
          break;

        case DRUPAL_BOOTSTRAP_VARIABLES:
          _drupal_bootstrap_variables();
          break;

        case DRUPAL_BOOTSTRAP_SESSION:
          require_once DRUPAL_ROOT . '/' . variable_get('session_inc', 'includes/session.inc');
          drupal_session_initialize();
          break;

        case DRUPAL_BOOTSTRAP_PAGE_HEADER:
          _drupal_bootstrap_page_header();
          break;

        case DRUPAL_BOOTSTRAP_LANGUAGE:
          drupal_language_initialize();
          break;

        case DRUPAL_BOOTSTRAP_FULL:
          require_once DRUPAL_ROOT . '/includes/common.inc';
          _drupal_bootstrap_full();
          break;
      }
    }
  }
  return $stored_phase;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
