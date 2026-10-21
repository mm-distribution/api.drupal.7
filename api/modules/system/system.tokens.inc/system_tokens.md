# system_tokens()

- **Type:** Function
- **File:** [`modules/system/system.tokens.inc`](_file.md), lines 131–269 · [local source](../../../../source/modules/system/system.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tokens.inc#L131-L269)
- **Module/theme:** system
- **Implements:** [hook_tokens()](../system.api.php/hook_tokens.md)

## Signature

```php
function system_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function system_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $url_options = array('absolute' => TRUE);
  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }
  $sanitize = !empty($options['sanitize']);

  $replacements = array();

  if ($type == 'site') {
    foreach ($tokens as $name => $original) {
      switch ($name) {
        case 'name':
          $site_name = variable_get('site_name', 'Drupal');
          $replacements[$original] = $sanitize ? check_plain($site_name) : $site_name;
          break;

        case 'slogan':
          $slogan = variable_get('site_slogan', '');
          $replacements[$original] = $sanitize ? check_plain($slogan) : $slogan;
          break;

        case 'mail':
          $replacements[$original] = variable_get('site_mail', '');
          break;

        case 'url':
          $replacements[$original] = url('<front>', $url_options);
          break;

        case 'url-brief':
          $replacements[$original] = preg_replace(array('!^https?://!', '!/$!'), '', url('<front>', $url_options));
          break;

        case 'login-url':
          $replacements[$original] = url('user', $url_options);
          break;
      }
    }
  }

  elseif ($type == 'date') {
    if (empty($data['date'])) {
      $date = REQUEST_TIME;
    }
    else {
      $date = $data['date'];
    }

    foreach ($tokens as $name => $original) {
      switch ($name) {
        case 'short':
          $replacements[$original] = format_date($date, 'short', '', NULL, $language_code);
          break;

        case 'medium':
          $replacements[$original] = format_date($date, 'medium', '', NULL, $language_code);
          break;

        case 'long':
          $replacements[$original] = format_date($date, 'long', '', NULL, $language_code);
          break;

        case 'since':
          $replacements[$original] = format_interval((REQUEST_TIME - $date), 2, $language_code);
          break;

        case 'raw':
          $replacements[$original] = $sanitize ? check_plain($date) : $date;
          break;
      }
    }

    if ($created_tokens = token_find_with_prefix($tokens, 'custom')) {
      foreach ($created_tokens as $name => $original) {
        $replacements[$original] = format_date($date, 'custom', $name, NULL, $language_code);
      }
    }
  }

  elseif ($type == 'file' && !empty($data['file'])) {
    $file = $data['file'];

    foreach ($tokens as $name => $original) {
      switch ($name) {
        // Basic keys and values.
        case 'fid':
          $replacements[$original] = $file->fid;
          break;

        // Essential file data
        case 'name':
          $replacements[$original] = $sanitize ? check_plain($file->filename) : $file->filename;
          break;

        case 'path':
          $replacements[$original] = $sanitize ? check_plain($file->uri) : $file->uri;
          break;

        case 'mime':
          $replacements[$original] = $sanitize ? check_plain($file->filemime) : $file->filemime;
          break;

        case 'size':
          $replacements[$original] = format_size($file->filesize);
          break;

        case 'url':
          $replacements[$original] = $sanitize ? check_plain(file_create_url($file->uri)) : file_create_url($file->uri);
          break;

        // These tokens are default variations on the chained tokens handled below.
        case 'timestamp':
          $replacements[$original] = format_date($file->timestamp, 'medium', '', NULL, $language_code);
          break;

        case 'owner':
          $account = user_load($file->uid);
          $name = format_username($account);
          $replacements[$original] = $sanitize ? check_plain($name) : $name;
          break;
      }
    }

    if ($date_tokens = token_find_with_prefix($tokens, 'timestamp')) {
      $replacements += token_generate('date', $date_tokens, array('date' => $file->timestamp), $options);
    }

    if (($owner_tokens = token_find_with_prefix($tokens, 'owner')) && $account = user_load($file->uid)) {
      $replacements += token_generate('user', $owner_tokens, array('user' => $account), $options);
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/system/system.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
