# includes/file.inc

- **Source:** [local](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · 2797 lines

## File documentation

```text
@file
API for handling file uploads and server file management.
```

## Functions (derived index)

- [file_get_stream_wrappers()](file_get_stream_wrappers.md) — Provides Drupal stream wrapper registry.
- [file_stream_wrapper_get_class()](file_stream_wrapper_get_class.md) — Returns the stream wrapper class name for a given scheme.
- [file_uri_scheme()](file_uri_scheme.md) — Returns the scheme of a URI (e.g. a stream).
- [file_stream_wrapper_valid_scheme()](file_stream_wrapper_valid_scheme.md) — Checks that the scheme of a stream URI is valid.
- [file_uri_target()](file_uri_target.md) — Returns the part of a URI after the schema.
- [file_default_scheme()](file_default_scheme.md) — Gets the default file stream implementation.
- [file_stream_wrapper_uri_normalize()](file_stream_wrapper_uri_normalize.md) — Normalizes a URI by making it syntactically correct.
- [file_stream_wrapper_get_instance_by_uri()](file_stream_wrapper_get_instance_by_uri.md) — Returns a reference to the stream wrapper class responsible for a given URI.
- [file_stream_wrapper_get_instance_by_scheme()](file_stream_wrapper_get_instance_by_scheme.md) — Returns a reference to the stream wrapper class responsible for a scheme.
- [file_create_url()](file_create_url.md) — Creates a web-accessible URL for a stream to an external or local file.
- [file_prepare_directory()](file_prepare_directory.md) — Checks that the directory exists and is writable.
- [file_ensure_htaccess()](file_ensure_htaccess.md) — Creates a .htaccess file in each Drupal files directory if it is missing.
- [file_create_htaccess()](file_create_htaccess.md) — Creates a .htaccess file in the given directory.
- [file_htaccess_lines()](file_htaccess_lines.md) — Returns the standard .htaccess lines that Drupal writes to file directories.
- [file_load_multiple()](file_load_multiple.md) — Loads file objects from the database.
- [file_load()](file_load.md) — Loads a single file object from the database.
- [file_save()](file_save.md) — Saves a file object to the database.
- [file_usage_list()](file_usage_list.md) — Determines where a file is used.
- [file_usage_add()](file_usage_add.md) — Records that a module is using a file.
- [file_usage_delete()](file_usage_delete.md) — Removes a record to indicate that a module is no longer using a file.
- [file_copy()](file_copy.md) — Copies a file to a new location and adds a file record to the database.
- [file_valid_uri()](file_valid_uri.md) — Determines whether the URI has a valid scheme for file API operations.
- [file_unmanaged_copy()](file_unmanaged_copy.md) — Copies a file to a new location without invoking the file API.
- [file_build_uri()](file_build_uri.md) — Constructs a URI to Drupal's default files location given a relative path.
- [file_destination()](file_destination.md) — Determines the destination path for a file.
- [file_move()](file_move.md) — Moves a file to a new location and update the file's database entry.
- [file_unmanaged_move()](file_unmanaged_move.md) — Moves a file to a new location without database changes or hook invocation.
- [file_munge_filename()](file_munge_filename.md) — Modifies a filename as needed for security purposes.
- [file_unmunge_filename()](file_unmunge_filename.md) — Undoes the effect of file_munge_filename().
- [file_create_filename()](file_create_filename.md) — Creates a full file path from a directory and filename.
- [file_delete()](file_delete.md) — Deletes a file and its database record.
- [file_unmanaged_delete()](file_unmanaged_delete.md) — Deletes a file without database changes or hook invocations.
- [file_unmanaged_delete_recursive()](file_unmanaged_delete_recursive.md) — Deletes all files and directories in the specified filepath recursively.
- [file_space_used()](file_space_used.md) — Determines total disk space used by a single user or the whole filesystem.
- [file_save_upload()](file_save_upload.md) — Saves a file upload to a new location.
- [drupal_move_uploaded_file()](drupal_move_uploaded_file.md) — Moves an uploaded file to a new location.
- [file_validate()](file_validate.md) — Checks that a file meets the criteria specified by the validators.
- [file_validate_name_length()](file_validate_name_length.md) — Checks for files with names longer than we can store in the database.
- [file_validate_extensions()](file_validate_extensions.md) — Checks that the filename ends with an allowed extension.
- [file_validate_size()](file_validate_size.md) — Checks that the file's size is below certain limits.
- [file_validate_is_image()](file_validate_is_image.md) — Checks that the file is recognized by image_get_info() as an image.
- [file_validate_image_resolution()](file_validate_image_resolution.md) — Verifies that image dimensions are within the specified maximum and minimum.
- [file_save_data()](file_save_data.md) — Saves a file to the specified destination and creates a database entry.
- [file_unmanaged_save_data()](file_unmanaged_save_data.md) — Saves a string to the specified destination without invoking file API.
- [file_transfer()](file_transfer.md) — Transfers a file to the client using HTTP.
- [file_download()](file_download.md) — Menu handler for private file transfers.
- [file_download_headers()](file_download_headers.md) — Retrieves headers for a private file download.
- [file_download_access()](file_download_access.md) — Checks that the current user has access to a particular file.
- [file_scan_directory()](file_scan_directory.md) — Finds all files that match a given mask in a given directory.
- [file_upload_max_size()](file_upload_max_size.md) — Determines the maximum file upload size by querying the PHP settings.
- [file_get_mimetype()](file_get_mimetype.md) — Determines an Internet Media Type or MIME type from a filename.
- [drupal_chmod()](drupal_chmod.md) — Sets the permissions on a file or directory.
- [drupal_unlink()](drupal_unlink.md) — Deletes a file.
- [drupal_realpath()](drupal_realpath.md) — Resolves the absolute filepath of a local URI or filepath.
- [drupal_dirname()](drupal_dirname.md) — Gets the name of the directory from a given path.
- [drupal_basename()](drupal_basename.md) — Gets the filename from a given path.
- [drupal_mkdir()](drupal_mkdir.md) — Creates a directory, optionally creating missing components in the path to the directory.
- [_drupal_mkdir_call()](_drupal_mkdir_call.md) — Helper function. Ensures we don't pass a NULL as a context resource to mkdir().
- [drupal_rmdir()](drupal_rmdir.md) — Removes a directory.
- [drupal_tempnam()](drupal_tempnam.md) — Creates a file with a unique filename in the specified directory.
- [file_directory_temp()](file_directory_temp.md) — Gets the path of system-appropriate temporary directory.
- [file_get_content_headers()](file_get_content_headers.md) — Examines a file object and returns appropriate content headers for download.
- [file_uri_normalize_dot_segments()](file_uri_normalize_dot_segments.md) — Normalize dot segments in a URI.

## Constants

### FILE_CREATE_DIRECTORY

- Line 41; topics: file

```php
define('FILE_CREATE_DIRECTORY', 1);
```

```text
Flag used by file_prepare_directory() -- create directory if not present.
```

### FILE_MODIFY_PERMISSIONS

- Line 46; topics: file

```php
define('FILE_MODIFY_PERMISSIONS', 2);
```

```text
Flag used by file_prepare_directory() -- file permissions may be changed.
```

### FILE_EXISTS_RENAME

- Line 51; topics: file

```php
define('FILE_EXISTS_RENAME', 0);
```

```text
Flag for dealing with existing files: Appends number until name is unique.
```

### FILE_EXISTS_REPLACE

- Line 56; topics: file

```php
define('FILE_EXISTS_REPLACE', 1);
```

```text
Flag for dealing with existing files: Replace the existing file.
```

### FILE_EXISTS_ERROR

- Line 61; topics: file

```php
define('FILE_EXISTS_ERROR', 2);
```

```text
Flag for dealing with existing files: Do nothing and return FALSE.
```

### FILE_STATUS_PERMANENT

- Line 70; topics: file

```php
define('FILE_STATUS_PERMANENT', 1);
```

```text
Indicates that the file is permanent and should not be deleted.

Temporary files older than DRUPAL_MAXIMUM_TEMP_FILE_AGE will be removed
during cron runs, but permanent files will not be removed during the file
garbage collection process.
```

### FILE_INSECURE_EXTENSIONS

- Line 77; topics: file

```php
define('FILE_INSECURE_EXTENSIONS', 'php|phar|pl|py|cgi|asp|js|phtml');
```

```text
A pipe-separated list of insecure extensions.

@see file_munge_filename(), file_save_upload()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
