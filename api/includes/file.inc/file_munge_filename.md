# file_munge_filename()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1180–1216 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1180-L1216)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_munge_filename($filename, $extensions, $alerts = TRUE)
```

## Documentation

```text
Modifies a filename as needed for security purposes.

Munging a file name prevents unknown file extensions from masking exploit
files. When web servers such as Apache decide how to process a URL request,
they use the file extension. If the extension is not recognized, Apache
skips that extension and uses the previous file extension. For example, if
the file being requested is exploit.php.pps, and Apache does not recognize
the '.pps' extension, it treats the file as PHP and executes it. To make
this file name safe for Apache and prevent it from executing as PHP, the
.php extension is "munged" into .php_, making the safe file name
exploit.php_.pps.

Specifically, this function adds an underscore to all extensions that are
between 2 and 5 characters in length, internal to the file name, and either
included in the list of unsafe extensions, or not included in $extensions.

Function behavior is also controlled by the Drupal variable
'allow_insecure_uploads'. If 'allow_insecure_uploads' evaluates to TRUE, no
alterations will be made, if it evaluates to FALSE, the filename is 'munged'.

@param $filename
  File name to modify.
@param $extensions
  A space-separated list of extensions that should not be altered. Note that
  extensions that are unsafe will be altered regardless of this parameter.
@param $alerts
  If TRUE, drupal_set_message() will be called to display a message if the
  file name was changed.

@return
  The potentially modified $filename.
```

## Code

```php
function file_munge_filename($filename, $extensions, $alerts = TRUE) {
  $original = $filename;

  // Allow potentially insecure uploads for very savvy users and admin
  if (!variable_get('allow_insecure_uploads', 0)) {
    // Remove any null bytes. See http://php.net/manual/security.filesystem.nullbytes.php
    $filename = str_replace(chr(0), '', $filename);

    $whitelist = array_unique(explode(' ', strtolower(trim($extensions))));

    // Remove unsafe extensions from the list of allowed extensions.
    $whitelist = array_diff($whitelist, explode('|', FILE_INSECURE_EXTENSIONS));

    // Split the filename up by periods. The first part becomes the basename
    // the last part the final extension.
    $filename_parts = explode('.', $filename);
    $new_filename = array_shift($filename_parts); // Remove file basename.
    $final_extension = array_pop($filename_parts); // Remove final extension.

    // Loop through the middle parts of the name and add an underscore to the
    // end of each section that could be a file extension but isn't in the list
    // of allowed extensions.
    foreach ($filename_parts as $filename_part) {
      $new_filename .= '.' . $filename_part;
      if (!in_array(strtolower($filename_part), $whitelist) && preg_match("/^[a-zA-Z]{2,5}\d?$/", $filename_part)) {
        $new_filename .= '_';
      }
    }
    $filename = $new_filename . '.' . $final_extension;

    if ($alerts && $original != $filename) {
      drupal_set_message(t('For security reasons, your upload has been renamed to %filename.', array('%filename' => $filename)));
    }
  }

  return $filename;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
