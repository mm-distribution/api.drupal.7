# file_get_stream_wrappers()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 130–178 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L130-L178)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_get_stream_wrappers($filter = STREAM_WRAPPERS_ALL)
```

## Documentation

```text
Provides Drupal stream wrapper registry.

A stream wrapper is an abstraction of a file system that allows Drupal to
use the same set of methods to access both local files and remote resources.

Provide a facility for managing and querying user-defined stream wrappers
in PHP. PHP's internal stream_get_wrappers() doesn't return the class
registered to handle a stream, which we need to be able to find the handler
for class instantiation.

If a module registers a scheme that is already registered with PHP, the
existing scheme will be unregistered and replaced with the specified class.

A stream is referenced as "scheme://target".

The optional $filter parameter can be used to retrieve only the stream
wrappers that are appropriate for particular usage. For example, this returns
only stream wrappers that use local file storage:
@code
  $local_stream_wrappers = file_get_stream_wrappers(STREAM_WRAPPERS_LOCAL);
@endcode

The $filter parameter can only filter to types containing a particular flag.
In some cases, you may want to filter to types that do not contain a
particular flag. For example, you may want to retrieve all stream wrappers
that are not writable, or all stream wrappers that are not local. PHP's
array_diff_key() function can be used to help with this. For example, this
returns only stream wrappers that do not use local file storage:
@code
  $remote_stream_wrappers = array_diff_key(file_get_stream_wrappers(STREAM_WRAPPERS_ALL), file_get_stream_wrappers(STREAM_WRAPPERS_LOCAL));
@endcode

@param $filter
  (Optional) Filters out all types except those with an on bit for each on
  bit in $filter. For example, if $filter is STREAM_WRAPPERS_WRITE_VISIBLE,
  which is equal to (STREAM_WRAPPERS_READ | STREAM_WRAPPERS_WRITE |
  STREAM_WRAPPERS_VISIBLE), then only stream wrappers with all three of these
  bits set are returned. Defaults to STREAM_WRAPPERS_ALL, which returns all
  registered stream wrappers.

@return
  An array keyed by scheme, with values containing an array of information
  about the stream wrapper, as returned by hook_stream_wrappers(). If $filter
  is omitted or set to STREAM_WRAPPERS_ALL, the entire Drupal stream wrapper
  registry is returned. Otherwise only the stream wrappers whose 'type'
  bitmask has an on bit for each bit specified in $filter are returned.

@see hook_stream_wrappers()
@see hook_stream_wrappers_alter()
```

## Code

```php
function file_get_stream_wrappers($filter = STREAM_WRAPPERS_ALL) {
  $wrappers_storage = &drupal_static(__FUNCTION__);

  if (!isset($wrappers_storage)) {
    $wrappers = module_invoke_all('stream_wrappers');
    foreach ($wrappers as $scheme => $info) {
      // Add defaults.
      $wrappers[$scheme] += array('type' => STREAM_WRAPPERS_NORMAL);
    }
    drupal_alter('stream_wrappers', $wrappers);
    $existing = stream_get_wrappers();
    foreach ($wrappers as $scheme => $info) {
      // We only register classes that implement our interface.
      if (in_array('DrupalStreamWrapperInterface', class_implements($info['class']), TRUE)) {
        // Record whether we are overriding an existing scheme.
        if (in_array($scheme, $existing, TRUE)) {
          $wrappers[$scheme]['override'] = TRUE;
          stream_wrapper_unregister($scheme);
        }
        else {
          $wrappers[$scheme]['override'] = FALSE;
        }
        if (($info['type'] & STREAM_WRAPPERS_LOCAL) == STREAM_WRAPPERS_LOCAL) {
          stream_wrapper_register($scheme, $info['class']);
        }
        else {
          stream_wrapper_register($scheme, $info['class'], STREAM_IS_URL);
        }
      }
      // Pre-populate the static cache with the filters most typically used.
      $wrappers_storage[STREAM_WRAPPERS_ALL][$scheme] = $wrappers[$scheme];
      if (($info['type'] & STREAM_WRAPPERS_WRITE_VISIBLE) == STREAM_WRAPPERS_WRITE_VISIBLE) {
        $wrappers_storage[STREAM_WRAPPERS_WRITE_VISIBLE][$scheme] = $wrappers[$scheme];
      }
    }
  }

  if (!isset($wrappers_storage[$filter])) {
    $wrappers_storage[$filter] = array();
    foreach ($wrappers_storage[STREAM_WRAPPERS_ALL] as $scheme => $info) {
      // Bit-wise filter.
      if (($info['type'] & $filter) == $filter) {
        $wrappers_storage[$filter][$scheme] = $info;
      }
    }
  }

  return $wrappers_storage[$filter];
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
