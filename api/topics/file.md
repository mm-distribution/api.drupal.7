# File interface

- **Topic id:** `file`
- **Defined in:** [`includes/file.inc`](../includes/file.inc/_file.md), line 17 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L17)

## Documentation

```text
@defgroup file File interface
@{
Common file handling functions.

Fields on the file object:
- fid: File ID
- uid: The {users}.uid of the user who is associated with the file.
- filename: Name of the file with no path components. This may differ from
  the basename of the filepath if the file is renamed to avoid overwriting
  an existing file.
- uri: URI of the file.
- filemime: The file's MIME type.
- filesize: The size of the file in bytes.
- status: A bitmapped field indicating the status of the file. The first 8
  bits are reserved for Drupal core. The least significant bit indicates
  temporary (0) or permanent (1). Temporary files older than
  DRUPAL_MAXIMUM_TEMP_FILE_AGE will be removed during cron runs.
- timestamp: UNIX timestamp for the date the file was added to the database.
```

## Members (derived, 70)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_drupal_mkdir_call()](../includes/file.inc/_drupal_mkdir_call.md) (function) — Helper function. Ensures we don't pass a NULL as a context resource to mkdir().
- [drupal_basename()](../includes/file.inc/drupal_basename.md) (function) — Gets the filename from a given path.
- [drupal_chmod()](../includes/file.inc/drupal_chmod.md) (function) — Sets the permissions on a file or directory.
- [drupal_dirname()](../includes/file.inc/drupal_dirname.md) (function) — Gets the name of the directory from a given path.
- [drupal_mkdir()](../includes/file.inc/drupal_mkdir.md) (function) — Creates a directory, optionally creating missing components in the path to the directory.
- [drupal_move_uploaded_file()](../includes/file.inc/drupal_move_uploaded_file.md) (function) — Moves an uploaded file to a new location.
- [drupal_realpath()](../includes/file.inc/drupal_realpath.md) (function) — Resolves the absolute filepath of a local URI or filepath.
- [drupal_rmdir()](../includes/file.inc/drupal_rmdir.md) (function) — Removes a directory.
- [drupal_tempnam()](../includes/file.inc/drupal_tempnam.md) (function) — Creates a file with a unique filename in the specified directory.
- [drupal_unlink()](../includes/file.inc/drupal_unlink.md) (function) — Deletes a file.
- [file_build_uri()](../includes/file.inc/file_build_uri.md) (function) — Constructs a URI to Drupal's default files location given a relative path.
- [file_copy()](../includes/file.inc/file_copy.md) (function) — Copies a file to a new location and adds a file record to the database.
- [file_create_filename()](../includes/file.inc/file_create_filename.md) (function) — Creates a full file path from a directory and filename.
- [file_create_htaccess()](../includes/file.inc/file_create_htaccess.md) (function) — Creates a .htaccess file in the given directory.
- [file_create_url()](../includes/file.inc/file_create_url.md) (function) — Creates a web-accessible URL for a stream to an external or local file.
- [file_default_scheme()](../includes/file.inc/file_default_scheme.md) (function) — Gets the default file stream implementation.
- [file_delete()](../includes/file.inc/file_delete.md) (function) — Deletes a file and its database record.
- [file_destination()](../includes/file.inc/file_destination.md) (function) — Determines the destination path for a file.
- [file_directory_temp()](../includes/file.inc/file_directory_temp.md) (function) — Gets the path of system-appropriate temporary directory.
- [file_download()](../includes/file.inc/file_download.md) (function) — Menu handler for private file transfers.
- [file_download_access()](../includes/file.inc/file_download_access.md) (function) — Checks that the current user has access to a particular file.
- [file_download_headers()](../includes/file.inc/file_download_headers.md) (function) — Retrieves headers for a private file download.
- [file_ensure_htaccess()](../includes/file.inc/file_ensure_htaccess.md) (function) — Creates a .htaccess file in each Drupal files directory if it is missing.
- [file_get_content_headers()](../includes/file.inc/file_get_content_headers.md) (function) — Examines a file object and returns appropriate content headers for download.
- [file_get_mimetype()](../includes/file.inc/file_get_mimetype.md) (function) — Determines an Internet Media Type or MIME type from a filename.
- [file_get_stream_wrappers()](../includes/file.inc/file_get_stream_wrappers.md) (function) — Provides Drupal stream wrapper registry.
- [file_htaccess_lines()](../includes/file.inc/file_htaccess_lines.md) (function) — Returns the standard .htaccess lines that Drupal writes to file directories.
- [file_load()](../includes/file.inc/file_load.md) (function) — Loads a single file object from the database.
- [file_load_multiple()](../includes/file.inc/file_load_multiple.md) (function) — Loads file objects from the database.
- [file_move()](../includes/file.inc/file_move.md) (function) — Moves a file to a new location and update the file's database entry.
- [file_munge_filename()](../includes/file.inc/file_munge_filename.md) (function) — Modifies a filename as needed for security purposes.
- [file_prepare_directory()](../includes/file.inc/file_prepare_directory.md) (function) — Checks that the directory exists and is writable.
- [file_save()](../includes/file.inc/file_save.md) (function) — Saves a file object to the database.
- [file_save_data()](../includes/file.inc/file_save_data.md) (function) — Saves a file to the specified destination and creates a database entry.
- [file_save_upload()](../includes/file.inc/file_save_upload.md) (function) — Saves a file upload to a new location.
- [file_scan_directory()](../includes/file.inc/file_scan_directory.md) (function) — Finds all files that match a given mask in a given directory.
- [file_space_used()](../includes/file.inc/file_space_used.md) (function) — Determines total disk space used by a single user or the whole filesystem.
- [file_stream_wrapper_get_class()](../includes/file.inc/file_stream_wrapper_get_class.md) (function) — Returns the stream wrapper class name for a given scheme.
- [file_stream_wrapper_get_instance_by_scheme()](../includes/file.inc/file_stream_wrapper_get_instance_by_scheme.md) (function) — Returns a reference to the stream wrapper class responsible for a scheme.
- [file_stream_wrapper_get_instance_by_uri()](../includes/file.inc/file_stream_wrapper_get_instance_by_uri.md) (function) — Returns a reference to the stream wrapper class responsible for a given URI.
- [file_stream_wrapper_uri_normalize()](../includes/file.inc/file_stream_wrapper_uri_normalize.md) (function) — Normalizes a URI by making it syntactically correct.
- [file_stream_wrapper_valid_scheme()](../includes/file.inc/file_stream_wrapper_valid_scheme.md) (function) — Checks that the scheme of a stream URI is valid.
- [file_transfer()](../includes/file.inc/file_transfer.md) (function) — Transfers a file to the client using HTTP.
- [file_unmanaged_copy()](../includes/file.inc/file_unmanaged_copy.md) (function) — Copies a file to a new location without invoking the file API.
- [file_unmanaged_delete()](../includes/file.inc/file_unmanaged_delete.md) (function) — Deletes a file without database changes or hook invocations.
- [file_unmanaged_delete_recursive()](../includes/file.inc/file_unmanaged_delete_recursive.md) (function) — Deletes all files and directories in the specified filepath recursively.
- [file_unmanaged_move()](../includes/file.inc/file_unmanaged_move.md) (function) — Moves a file to a new location without database changes or hook invocation.
- [file_unmanaged_save_data()](../includes/file.inc/file_unmanaged_save_data.md) (function) — Saves a string to the specified destination without invoking file API.
- [file_unmunge_filename()](../includes/file.inc/file_unmunge_filename.md) (function) — Undoes the effect of file_munge_filename().
- [file_upload_max_size()](../includes/file.inc/file_upload_max_size.md) (function) — Determines the maximum file upload size by querying the PHP settings.
- [file_uri_normalize_dot_segments()](../includes/file.inc/file_uri_normalize_dot_segments.md) (function) — Normalize dot segments in a URI.
- [file_uri_scheme()](../includes/file.inc/file_uri_scheme.md) (function) — Returns the scheme of a URI (e.g. a stream).
- [file_uri_target()](../includes/file.inc/file_uri_target.md) (function) — Returns the part of a URI after the schema.
- [file_usage_add()](../includes/file.inc/file_usage_add.md) (function) — Records that a module is using a file.
- [file_usage_delete()](../includes/file.inc/file_usage_delete.md) (function) — Removes a record to indicate that a module is no longer using a file.
- [file_usage_list()](../includes/file.inc/file_usage_list.md) (function) — Determines where a file is used.
- [file_valid_uri()](../includes/file.inc/file_valid_uri.md) (function) — Determines whether the URI has a valid scheme for file API operations.
- [file_validate()](../includes/file.inc/file_validate.md) (function) — Checks that a file meets the criteria specified by the validators.
- [file_validate_extensions()](../includes/file.inc/file_validate_extensions.md) (function) — Checks that the filename ends with an allowed extension.
- [file_validate_image_resolution()](../includes/file.inc/file_validate_image_resolution.md) (function) — Verifies that image dimensions are within the specified maximum and minimum.
- [file_validate_is_image()](../includes/file.inc/file_validate_is_image.md) (function) — Checks that the file is recognized by image_get_info() as an image.
- [file_validate_name_length()](../includes/file.inc/file_validate_name_length.md) (function) — Checks for files with names longer than we can store in the database.
- [file_validate_size()](../includes/file.inc/file_validate_size.md) (function) — Checks that the file's size is below certain limits.
- [FILE_CREATE_DIRECTORY](../includes/file.inc/_file.md#file_create_directory) (constant) — Flag used by file_prepare_directory() -- create directory if not present.
- [FILE_EXISTS_ERROR](../includes/file.inc/_file.md#file_exists_error) (constant) — Flag for dealing with existing files: Do nothing and return FALSE.
- [FILE_EXISTS_RENAME](../includes/file.inc/_file.md#file_exists_rename) (constant) — Flag for dealing with existing files: Appends number until name is unique.
- [FILE_EXISTS_REPLACE](../includes/file.inc/_file.md#file_exists_replace) (constant) — Flag for dealing with existing files: Replace the existing file.
- [FILE_INSECURE_EXTENSIONS](../includes/file.inc/_file.md#file_insecure_extensions) (constant) — A pipe-separated list of insecure extensions.
- [FILE_MODIFY_PERMISSIONS](../includes/file.inc/_file.md#file_modify_permissions) (constant) — Flag used by file_prepare_directory() -- file permissions may be changed.
- [FILE_STATUS_PERMANENT](../includes/file.inc/_file.md#file_status_permanent) (constant) — Indicates that the file is permanent and should not be deleted.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
