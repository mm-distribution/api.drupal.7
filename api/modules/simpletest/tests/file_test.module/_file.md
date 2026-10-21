# modules/simpletest/tests/file_test.module

- **Source:** [local](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · 470 lines
- **Module/theme:** batch_test

## File documentation

```text
@file
Helper module for the file tests.

The caller is must call file_test_reset() to initializing this module before
calling file_test_get_calls() or file_test_set_return().
```

## Functions (derived index)

- [file_test_menu()](file_test_menu.md) — Implements hook_menu().
- [file_test_stream_wrappers()](file_test_stream_wrappers.md) — Implements hook_stream_wrappers().
- [_file_test_form()](_file_test_form.md) — Form to test file uploads.
- [_file_test_form_submit()](_file_test_form_submit.md) — Process the upload.
- [file_test_reset()](file_test_reset.md) — Reset/initialize the history of calls to the file_* hooks.
- [file_test_get_calls()](file_test_get_calls.md) — Get the arguments passed to invocation of a given hook since file_test_reset() was last called.
- [file_test_get_all_calls()](file_test_get_all_calls.md) — Get an array with the calls for all hooks.
- [_file_test_log_call()](_file_test_log_call.md) — Store the values passed to a hook invocation.
- [_file_test_get_return()](_file_test_get_return.md) — Load the appropriate return value.
- [file_test_set_return()](file_test_set_return.md) — Assign a return value for a given operation.
- [file_test_file_load()](file_test_file_load.md) — Implements hook_file_load().
- [file_test_file_validate()](file_test_file_validate.md) — Implements hook_file_validate().
- [file_test_file_download()](file_test_file_download.md) — Implements hook_file_download().
- [file_test_file_insert()](file_test_file_insert.md) — Implements hook_file_insert().
- [file_test_file_update()](file_test_file_update.md) — Implements hook_file_update().
- [file_test_file_copy()](file_test_file_copy.md) — Implements hook_file_copy().
- [file_test_file_move()](file_test_file_move.md) — Implements hook_file_move().
- [file_test_file_delete()](file_test_file_delete.md) — Implements hook_file_delete().
- [file_test_file_url_alter()](file_test_file_url_alter.md) — Implements hook_file_url_alter().
- [file_test_file_mimetype_mapping_alter()](file_test_file_mimetype_mapping_alter.md) — Implements hook_file_mimetype_mapping_alter().

## Classes and interfaces (derived index)

- [DrupalDummyStreamWrapper](DrupalDummyStreamWrapper.md) — Helper class for testing the stream wrapper registry.
- [DrupalDummyRemoteStreamWrapper](DrupalDummyRemoteStreamWrapper.md) — Helper class for testing the stream wrapper registry.

## Constants

### FILE_URL_TEST_CDN_1

- Line 12

```php
define('FILE_URL_TEST_CDN_1', 'http://cdn1.example.com');
```

### FILE_URL_TEST_CDN_2

- Line 13

```php
define('FILE_URL_TEST_CDN_2', 'http://cdn2.example.com');
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
