# install_select_locale()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1232–1315 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1232-L1315)

## Signature

```php
function install_select_locale(&$install_state)
```

## Documentation

```text
Installation task; select which locale to use for the current profile.

@param $install_state
  An array of information about the current installation state. The chosen
  locale will be added here, if it was not already selected previously, as
  will a list of all available locales.

@return
  For interactive installations, a form or other page output allowing the
  locale to be selected or providing information about locale selection, if
  a locale has not been chosen. Otherwise, an exception is thrown if a
  locale cannot be chosen automatically.
```

## Code

```php
function install_select_locale(&$install_state) {
  // Find all available locales.
  $profilename = $install_state['parameters']['profile'];
  $locales = install_find_locales($profilename);
  $install_state['locales'] += $locales;

  if (!empty($_POST['locale'])) {
    foreach ($locales as $locale) {
      if ($_POST['locale'] == $locale->langcode) {
        $install_state['parameters']['locale'] = $locale->langcode;
        return;
      }
    }
  }

  if (empty($install_state['parameters']['locale'])) {
    // If only the built-in (English) language is available, and we are
    // performing an interactive installation, inform the user that the
    // installer can be localized. Otherwise we assume the user knows what he
    // is doing.
    if (count($locales) == 1) {
      if ($install_state['interactive']) {
        drupal_set_title(st('Choose language'));
        if (!empty($install_state['parameters']['localize'])) {
          $output = '<p>Follow these steps to translate Drupal into your language:</p>';
          $output .= '<ol>';
          $output .= '<li>Download a translation from the <a href="http://localize.drupal.org/download" target="_blank">translation server</a>.</li>';
          $output .= '<li>Place it into the following directory:
<pre>
/profiles/' . $profilename . '/translations/
</pre></li>';
          $output .= '</ol>';
          $output .= '<p>For more information on installing Drupal in different languages, visit the <a href="http://drupal.org/localize" target="_blank">drupal.org handbook page</a>.</p>';
          $output .= '<p>How should the installation continue?</p>';
          $output .= '<ul>';
          $output .= '<li><a href="install.php?profile=' . $profilename . '">Reload the language selection page after adding translations</a></li>';
          $output .= '<li><a href="install.php?profile=' . $profilename . '&amp;locale=en">Continue installation in English</a></li>';
          $output .= '</ul>';
        }
        else {
          include_once DRUPAL_ROOT . '/includes/form.inc';
          $elements = drupal_get_form('install_select_locale_form', $locales, $profilename);
          $output = drupal_render($elements);
        }
        return $output;
      }
      // One language, but not an interactive installation. Assume the user
      // knows what he is doing.
      $locale = current($locales);
      $install_state['parameters']['locale'] = $locale->name;
      return;
    }
    else {
      // Allow profile to pre-select the language, skipping the selection.
      $function = $profilename . '_profile_details';
      if (function_exists($function)) {
        $details = $function();
        if (isset($details['language'])) {
          foreach ($locales as $locale) {
            if ($details['language'] == $locale->name) {
              $install_state['parameters']['locale'] = $locale->name;
              return;
            }
          }
        }
      }

      // We still don't have a locale, so display a form for selecting one.
      // Only do this in the case of interactive installations, since this is
      // not a real form with submit handlers (the database isn't even set up
      // yet), rather just a convenience method for setting parameters in the
      // URL.
      if ($install_state['interactive']) {
        drupal_set_title(st('Choose language'));
        include_once DRUPAL_ROOT . '/includes/form.inc';
        $elements = drupal_get_form('install_select_locale_form', $locales, $profilename);
        return drupal_render($elements);
      }
      else {
        throw new Exception(st('Sorry, you must select a language to continue the installation.'));
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
