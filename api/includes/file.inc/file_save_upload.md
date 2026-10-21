# file_save_upload()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1488–1685 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1488-L1685)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_save_upload($form_field_name, $validators = array(), $destination = FALSE, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Saves a file upload to a new location.

The file will be added to the {file_managed} table as a temporary file.
Temporary files are periodically cleaned. To make the file a permanent file,
assign the status and use file_save() to save the changes.

@param $form_field_name
  A string that is the associative array key of the upload form element in
  the form array.
@param $validators
  An optional, associative array of callback functions used to validate the
  file. See file_validate() for a full discussion of the array format.
  If no extension validator is provided it will default to a limited safe
  list of extensions which is as follows: "jpg jpeg gif png txt
  doc xls pdf ppt pps odt ods odp". To allow all extensions you must
  explicitly set the 'file_validate_extensions' validator to an empty array
  (Beware: this is not safe and should only be allowed for trusted users, if
  at all).
@param $destination
  A string containing the URI that the file should be copied to. This must
  be a stream wrapper URI. If this value is omitted, Drupal's temporary
  files scheme will be used ("temporary://").
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE: Replace the existing file.
  - FILE_EXISTS_RENAME: Append _{incrementing number} until the filename is
    unique.
  - FILE_EXISTS_ERROR: Do nothing and return FALSE.

@return
  An object containing the file information if the upload succeeded, FALSE
  in the event of an error, or NULL if no file was uploaded. The
  documentation for the "File interface" group, which you can find under
  Related topics, or the header at the top of this file, documents the
  components of a file object. In addition to the standard components,
  this function adds:
  - source: Path to the file before it is moved.
  - destination: Path to the file after it is moved (same as 'uri').
```

## Code

```php
function file_save_upload($form_field_name, $validators = array(), $destination = FALSE, $replace = FILE_EXISTS_RENAME) {
  global $user;
  static $upload_cache;

  // Return cached objects without processing since the file will have
  // already been processed and the paths in _FILES will be invalid.
  if (isset($upload_cache[$form_field_name])) {
    return $upload_cache[$form_field_name];
  }

  // Make sure there's an upload to process.
  if (empty($_FILES['files']['name'][$form_field_name])) {
    return NULL;
  }

  // Check for file upload errors and return FALSE if a lower level system
  // error occurred. For a complete list of errors:
  // See http://php.net/manual/features.file-upload.errors.php.
  switch ($_FILES['files']['error'][$form_field_name]) {
    case UPLOAD_ERR_INI_SIZE:
    case UPLOAD_ERR_FORM_SIZE:
      drupal_set_message(t('The file %file could not be saved, because it exceeds %maxsize, the maximum allowed size for uploads.', array('%file' => $_FILES['files']['name'][$form_field_name], '%maxsize' => format_size(file_upload_max_size()))), 'error');
      return FALSE;

    case UPLOAD_ERR_PARTIAL:
    case UPLOAD_ERR_NO_FILE:
      drupal_set_message(t('The file %file could not be saved, because the upload did not complete.', array('%file' => $_FILES['files']['name'][$form_field_name])), 'error');
      return FALSE;

    case UPLOAD_ERR_OK:
      // Final check that this is a valid upload, if it isn't, use the
      // default error handler.
      if (is_uploaded_file($_FILES['files']['tmp_name'][$form_field_name])) {
        break;
      }

    // Unknown error
    default:
      drupal_set_message(t('The file %file could not be saved. An unknown error has occurred.', array('%file' => $_FILES['files']['name'][$form_field_name])), 'error');
      return FALSE;
  }

  // Begin building file object.
  $file = new stdClass();
  $file->uid      = $user->uid;
  $file->status   = 0;
  $file->filename = trim(drupal_basename($_FILES['files']['name'][$form_field_name]), '.');
  $file->uri      = $_FILES['files']['tmp_name'][$form_field_name];
  $file->filemime = file_get_mimetype($file->filename);
  $file->filesize = $_FILES['files']['size'][$form_field_name];

  $extensions = '';
  if (isset($validators['file_validate_extensions'])) {
    if (isset($validators['file_validate_extensions'][0])) {
      // Build the list of non-munged extensions if the caller provided them.
      $extensions = $validators['file_validate_extensions'][0];
    }
    else {
      // If 'file_validate_extensions' is set and the list is empty then the
      // caller wants to allow any extension. In this case we have to remove the
      // validator or else it will reject all extensions.
      unset($validators['file_validate_extensions']);
    }
  }
  else {
    // No validator was provided, so add one using the default list.
    // Build a default non-munged safe list for file_munge_filename().
    $extensions = 'jpg jpeg gif png txt doc xls pdf ppt pps odt ods odp';
    $validators['file_validate_extensions'] = array();
    $validators['file_validate_extensions'][0] = $extensions;
  }

  if (!variable_get('allow_insecure_uploads', 0)) {
    if (!empty($extensions)) {
      // Munge the filename to protect against possible malicious extension hiding
      // within an unknown file type (ie: filename.html.foo).
      $file->filename = file_munge_filename($file->filename, $extensions);
    }

    // Rename potentially executable files, to help prevent exploits (i.e. will
    // rename filename.php.foo and filename.php to filename.php_.foo_.txt and
    // filename.php_.txt, respectively). Don't rename if 'allow_insecure_uploads'
    // evaluates to TRUE.
    if (preg_match('/\.(' . FILE_INSECURE_EXTENSIONS . ')(\.|$)/i', $file->filename)) {
      // If the file will be rejected anyway due to a disallowed extension, it
      // should not be renamed; rather, we'll let file_validate_extensions()
      // reject it below.
      if (!isset($validators['file_validate_extensions']) || !file_validate_extensions($file, $extensions)) {
        $file->filemime = 'text/plain';
        if (substr($file->filename, -4) != '.txt') {
          // The destination filename will also later be used to create the URI.
          $file->filename .= '.txt';
        }
        $file->filename = file_munge_filename($file->filename, $extensions, FALSE);
        drupal_set_message(t('For security reasons, your upload has been renamed to %filename.', array('%filename' => $file->filename)));
        // The .txt extension may not be in the allowed list of extensions. We have
        // to add it here or else the file upload will fail.
        if (!empty($validators['file_validate_extensions'][0])) {
          $validators['file_validate_extensions'][0] .= ' txt';
        }
      }
    }
  }

  // If the destination is not provided, use the temporary directory.
  if (empty($destination)) {
    $destination = 'temporary://';
  }

  // Assert that the destination contains a valid stream.
  $destination_scheme = file_uri_scheme($destination);
  if (!$destination_scheme || !file_stream_wrapper_valid_scheme($destination_scheme)) {
    drupal_set_message(t('The file could not be uploaded, because the destination %destination is invalid.', array('%destination' => $destination)), 'error');
    return FALSE;
  }

  $file->source = $form_field_name;
  // A URI may already have a trailing slash or look like "public://".
  if (substr($destination, -1) != '/') {
    $destination .= '/';
  }
  try {
    $file->destination = file_destination($destination . $file->filename, $replace);
  }
  catch (RuntimeException $e) {
    drupal_set_message(t('The file %source could not be uploaded because the name is invalid.', array('%source' => $form_field_name)), 'error');
    return FALSE;
  }
  // If file_destination() returns FALSE then $replace == FILE_EXISTS_ERROR and
  // there's an existing file so we need to bail.
  if ($file->destination === FALSE) {
    drupal_set_message(t('The file %source could not be uploaded because a file by that name already exists in the destination %directory.', array('%source' => $form_field_name, '%directory' => $destination)), 'error');
    return FALSE;
  }

  // Add in our check of the file name length.
  $validators['file_validate_name_length'] = array();

  // Call the validation functions specified by this function's caller.
  $errors = file_validate($file, $validators);

  // Check for errors.
  if (!empty($errors)) {
    $message = t('The specified file %name could not be uploaded.', array('%name' => $file->filename));
    if (count($errors) > 1) {
      $message .= theme('item_list', array('items' => $errors));
    }
    else {
      $message .= ' ' . array_pop($errors);
    }
    form_set_error($form_field_name, $message);
    return FALSE;
  }

  // Move uploaded files from PHP's upload_tmp_dir to Drupal's temporary
  // directory. This overcomes open_basedir restrictions for future file
  // operations.
  $file->uri = $file->destination;
  if (!drupal_move_uploaded_file($_FILES['files']['tmp_name'][$form_field_name], $file->uri)) {
    form_set_error($form_field_name, t('File upload error. Could not move uploaded file.'));
    watchdog('file', 'Upload error. Could not move uploaded file %file to destination %destination.', array('%file' => $file->filename, '%destination' => $file->uri));
    return FALSE;
  }

  // Set the permissions on the new file.
  drupal_chmod($file->uri);

  // If we are replacing an existing file re-use its database record.
  if ($replace == FILE_EXISTS_REPLACE) {
    $existing_files = file_load_multiple(array(), array('uri' => $file->uri));
    if (count($existing_files)) {
      $existing = reset($existing_files);
      $file->fid = $existing->fid;
    }
  }

  // If we made it this far it's safe to record this file in the database.
  if ($file = file_save($file)) {
    // Track non-public files in the session if they were uploaded by an
    // anonymous user. This allows modules such as the File module to only
    // grant view access to the specific anonymous user who uploaded the file.
    // See file_file_download().
    // The 'file_public_schema' variable is used to allow other publicly
    // accessible file schemes to be treated the same as the public:// scheme
    // provided by Drupal core and to avoid adding unnecessary data to the
    // session (and the resulting bypass of the page cache) in those cases. For
    // security reasons, only schemes that are completely publicly accessible,
    // with no download restrictions, should be added to this variable. See
    // file_managed_file_value().
    if (!$user->uid && !in_array($destination_scheme, variable_get('file_public_schema', array('public')))) {
      $_SESSION['anonymous_allowed_file_ids'][$file->fid] = $file->fid;
    }
    // Add file to the cache.
    $upload_cache[$form_field_name] = $file;
    return $file;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
