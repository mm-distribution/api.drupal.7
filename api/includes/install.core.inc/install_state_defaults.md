# install_state_defaults()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 124–198 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L124-L198)

## Signature

```php
function install_state_defaults()
```

## Documentation

```text
Returns an array of default settings for the global installation state.

The installation state is initialized with these settings at the beginning
of each page request. They may evolve during the page request, but they are
initialized again once the next request begins.

Non-interactive Drupal installations can override some of these default
settings by passing in an array to the installation script, most notably
'parameters' (which contains one-time parameters such as 'profile' and
'locale' that are normally passed in via the URL) and 'forms' (which can
be used to programmatically submit forms during the installation; the keys
of each element indicate the name of the installation task that the form
submission is for, and the values are used as the $form_state['values']
array that is passed on to the form submission via drupal_form_submit()).

@see drupal_form_submit()
```

## Code

```php
function install_state_defaults() {
  $defaults = array(
    // The current task being processed.
    'active_task' => NULL,
    // The last task that was completed during the previous installation
    // request.
    'completed_task' => NULL,
    // This becomes TRUE only when Drupal's system module is installed.
    'database_tables_exist' => FALSE,
    // An array of forms to be programmatically submitted during the
    // installation. The keys of each element indicate the name of the
    // installation task that the form submission is for, and the values are
    // used as the $form_state['values'] array that is passed on to the form
    // submission via drupal_form_submit().
    'forms' => array(),
    // This becomes TRUE only at the end of the installation process, after
    // all available tasks have been completed and Drupal is fully installed.
    // It is used by the installer to store correct information in the database
    // about the completed installation, as well as to inform theme functions
    // that all tasks are finished (so that the task list can be displayed
    // correctly).
    'installation_finished' => FALSE,
    // Whether or not this installation is interactive. By default this will
    // be set to FALSE if settings are passed in to install_drupal().
    'interactive' => TRUE,
    // An array of available languages for the installation.
    'locales' => array(),
    // An array of parameters for the installation, pre-populated by the URL
    // or by the settings passed in to install_drupal(). This is primarily
    // used to store 'profile' (the name of the chosen installation profile)
    // and 'locale' (the name of the chosen installation language), since
    // these settings need to persist from page request to page request before
    // the database is available for storage.
    'parameters' => array(),
    // Whether or not the parameters have changed during the current page
    // request. For interactive installations, this will trigger a page
    // redirect.
    'parameters_changed' => FALSE,
    // An array of information about the chosen installation profile. This will
    // be filled in based on the profile's .info file.
    'profile_info' => array(),
    // An array of available installation profiles.
    'profiles' => array(),
    // An array of server variables that will be substituted into the global
    // $_SERVER array via drupal_override_server_variables(). Used by
    // non-interactive installations only.
    'server' => array(),
    // This becomes TRUE only when a valid database connection can be
    // established.
    'settings_verified' => FALSE,
    // Installation tasks can set this to TRUE to force the page request to
    // end (even if there is no themable output), in the case of an interactive
    // installation. This is needed only rarely; for example, it would be used
    // by an installation task that prints JSON output rather than returning a
    // themed page. The most common example of this is during batch processing,
    // but the Drupal installer automatically takes care of setting this
    // parameter properly in that case, so that individual installation tasks
    // which implement the batch API do not need to set it themselves.
    'stop_page_request' => FALSE,
    // Installation tasks can set this to TRUE to indicate that the task should
    // be run again, even if it normally wouldn't be. This can be used, for
    // example, if a single task needs to be spread out over multiple page
    // requests, or if it needs to perform some validation before allowing
    // itself to be marked complete. The most common examples of this are batch
    // processing and form submissions, but the Drupal installer automatically
    // takes care of setting this parameter properly in those cases, so that
    // individual installation tasks which implement the batch API or form API
    // do not need to set it themselves.
    'task_not_complete' => FALSE,
    // A list of installation tasks which have already been performed during
    // the current page request.
    'tasks_performed' => array(),
  );
  return $defaults;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
