# hook_stream_wrappers()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2777–2813 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2777-L2813)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_stream_wrappers()
```

## Documentation

```text
Registers PHP stream wrapper implementations associated with a module.

Provide a facility for managing and querying user-defined stream wrappers
in PHP. PHP's internal stream_get_wrappers() doesn't return the class
registered to handle a stream, which we need to be able to find the handler
for class instantiation.

If a module registers a scheme that is already registered with PHP, it will
be unregistered and replaced with the specified class.

@return
  A nested array, keyed first by scheme name ("public" for "public://"),
  then keyed by the following values:
  - 'name' A short string to name the wrapper.
  - 'class' A string specifying the PHP class that implements the
    DrupalStreamWrapperInterface interface.
  - 'description' A string with a short description of what the wrapper does.
  - 'type' (Optional) A bitmask of flags indicating what type of streams this
    wrapper will access - local or remote, readable and/or writeable, etc.
    Many shortcut constants are defined in stream_wrappers.inc. Defaults to
    STREAM_WRAPPERS_NORMAL which includes all of these bit flags:
    - STREAM_WRAPPERS_READ
    - STREAM_WRAPPERS_WRITE
    - STREAM_WRAPPERS_VISIBLE

@see file_get_stream_wrappers()
@see hook_stream_wrappers_alter()
@see system_stream_wrappers()
```

## Code

```php
function hook_stream_wrappers() {
  return array(
    'public' => array(
      'name' => t('Public files'),
      'class' => 'DrupalPublicStreamWrapper',
      'description' => t('Public local files served by the webserver.'),
      'type' => STREAM_WRAPPERS_LOCAL_NORMAL,
    ),
    'private' => array(
      'name' => t('Private files'),
      'class' => 'DrupalPrivateStreamWrapper',
      'description' => t('Private local files served by Drupal.'),
      'type' => STREAM_WRAPPERS_LOCAL_NORMAL,
    ),
    'temp' => array(
      'name' => t('Temporary files'),
      'class' => 'DrupalTempStreamWrapper',
      'description' => t('Temporary local files for upload and previews.'),
      'type' => STREAM_WRAPPERS_LOCAL_HIDDEN,
    ),
    'cdn' => array(
      'name' => t('Content delivery network files'),
      'class' => 'MyModuleCDNStreamWrapper',
      'description' => t('Files served by a content delivery network.'),
      // 'type' can be omitted to use the default of STREAM_WRAPPERS_NORMAL
    ),
    'youtube' => array(
      'name' => t('YouTube video'),
      'class' => 'MyModuleYouTubeStreamWrapper',
      'description' => t('Video streamed from YouTube.'),
      // A module implementing YouTube integration may decide to support using
      // the YouTube API for uploading video, but here, we assume that this
      // particular module only supports playing YouTube video.
      'type' => STREAM_WRAPPERS_READ_VISIBLE,
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_stream_wrappers()".

- [file_test_stream_wrappers()](../../simpletest/tests/file_test.module/file_test_stream_wrappers.md) — `modules/simpletest/tests/file_test.module`
- [system_stream_wrappers()](../system.module/system_stream_wrappers.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
