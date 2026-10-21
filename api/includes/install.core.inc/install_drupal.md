# install_drupal()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 64–104 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L64-L104)

## Signature

```php
function install_drupal($settings = array())
```

## Documentation

```text
Installs Drupal either interactively or via an array of passed-in settings.

The Drupal installation happens in a series of steps, which may be spread
out over multiple page requests. Each request begins by trying to determine
the last completed installation step (also known as a "task"), if one is
available from a previous request. Control is then passed to the task
handler, which processes the remaining tasks that need to be run until (a)
an error is thrown, (b) a new page needs to be displayed, or (c) the
installation finishes (whichever happens first).

@param $settings
  An optional array of installation settings. Leave this empty for a normal,
  interactive, browser-based installation intended to occur over multiple
  page requests. Alternatively, if an array of settings is passed in, the
  installer will attempt to use it to perform the installation in a single
  page request (optimized for the command line) and not send any output
  intended for the web browser. See install_state_defaults() for a list of
  elements that are allowed to appear in this array.

@see install_state_defaults()
```

## Code

```php
function install_drupal($settings = array()) {
  global $install_state;
  // Initialize the installation state with the settings that were passed in,
  // as well as a boolean indicating whether or not this is an interactive
  // installation.
  $interactive = empty($settings);
  $install_state = $settings + array('interactive' => $interactive) + install_state_defaults();
  try {
    // Begin the page request. This adds information about the current state of
    // the Drupal installation to the passed-in array.
    install_begin_request($install_state);
    // Based on the installation state, run the remaining tasks for this page
    // request, and collect any output.
    $output = install_run_tasks($install_state);
  }
  catch (Exception $e) {
    // When an installation error occurs, either send the error to the web
    // browser or pass on the exception so the calling script can use it.
    if ($install_state['interactive']) {
      install_display_output($e->getMessage(), $install_state);
    }
    else {
      throw $e;
    }
  }
  // All available tasks for this page request are now complete. Interactive
  // installations can send output to the browser or redirect the user to the
  // next page.
  if ($install_state['interactive']) {
    if ($install_state['parameters_changed']) {
      // Redirect to the correct page if the URL parameters have changed.
      install_goto(install_redirect_url($install_state));
    }
    elseif (isset($output)) {
      // Display a page only if some output is available. Otherwise it is
      // possible that we are printing a JSON page and theme output should
      // not be shown.
      install_display_output($output, $install_state);
    }
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
