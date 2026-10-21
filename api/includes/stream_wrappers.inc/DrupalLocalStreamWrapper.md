# DrupalLocalStreamWrapper

- **Type:** Class
- **File:** [`includes/stream_wrappers.inc`](_file.md), lines 233–912 · [local source](../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L233-L912)

## Signature

```php
abstract class DrupalLocalStreamWrapper implements DrupalStreamWrapperInterface
```

## Documentation

```text
Drupal stream wrapper base class for local files.

This class provides a complete stream wrapper implementation. URIs such as
"public://example.txt" are expanded to a normal filesystem path such as
"sites/default/files/example.txt" and then PHP filesystem functions are
invoked.

DrupalLocalStreamWrapper implementations need to implement at least the
getDirectoryPath() and getExternalUrl() methods.
```

## Properties

### $context

```php
public $context;
```

```text
Stream context resource.

@var Resource
```

### $handle

```php
public $handle = NULL;
```

```text
A generic resource handle.

@var Resource
```

### $uri

```php
protected $uri;
```

```text
Instance URI (stream).

A stream is referenced as "scheme://target".

@var String
```

## Methods (derived index)

- [getDirectoryPath()](DrupalLocalStreamWrapper/getDirectoryPath.md) — Gets the path that the wrapper is responsible for.
- [setUri()](DrupalLocalStreamWrapper/setUri.md) — Base implementation of setUri().
- [getUri()](DrupalLocalStreamWrapper/getUri.md) — Base implementation of getUri().
- [getTarget()](DrupalLocalStreamWrapper/getTarget.md) — Returns the local writable target of the resource within the stream.
- [getMimeType()](DrupalLocalStreamWrapper/getMimeType.md) — Base implementation of getMimeType().
- [chmod()](DrupalLocalStreamWrapper/chmod.md) — Base implementation of chmod().
- [realpath()](DrupalLocalStreamWrapper/realpath.md) — Base implementation of realpath().
- [getLocalPath()](DrupalLocalStreamWrapper/getLocalPath.md) — Returns the canonical absolute path of the URI, if possible.
- [stream_open()](DrupalLocalStreamWrapper/stream_open.md) — Support for fopen(), file_get_contents(), file_put_contents() etc.
- [stream_lock()](DrupalLocalStreamWrapper/stream_lock.md) — Support for flock().
- [stream_read()](DrupalLocalStreamWrapper/stream_read.md) — Support for fread(), file_get_contents() etc.
- [stream_write()](DrupalLocalStreamWrapper/stream_write.md) — Support for fwrite(), file_put_contents() etc.
- [stream_eof()](DrupalLocalStreamWrapper/stream_eof.md) — Support for feof().
- [stream_seek()](DrupalLocalStreamWrapper/stream_seek.md) — Support for fseek().
- [stream_flush()](DrupalLocalStreamWrapper/stream_flush.md) — Support for fflush().
- [stream_tell()](DrupalLocalStreamWrapper/stream_tell.md) — Support for ftell().
- [stream_stat()](DrupalLocalStreamWrapper/stream_stat.md) — Support for fstat().
- [stream_close()](DrupalLocalStreamWrapper/stream_close.md) — Support for fclose().
- [stream_metadata()](DrupalLocalStreamWrapper/stream_metadata.md) — Sets metadata on the stream.
- [stream_truncate()](DrupalLocalStreamWrapper/stream_truncate.md) — Truncate stream.
- [stream_cast()](DrupalLocalStreamWrapper/stream_cast.md) — Retrieve the underlying stream resource.
- [stream_set_option()](DrupalLocalStreamWrapper/stream_set_option.md) — Change stream options.
- [unlink()](DrupalLocalStreamWrapper/unlink.md) — Support for unlink().
- [rename()](DrupalLocalStreamWrapper/rename.md) — Support for rename().
- [dirname()](DrupalLocalStreamWrapper/dirname.md) — Gets the name of the directory from a given path.
- [mkdir()](DrupalLocalStreamWrapper/mkdir.md) — Support for mkdir().
- [rmdir()](DrupalLocalStreamWrapper/rmdir.md) — Support for rmdir().
- [url_stat()](DrupalLocalStreamWrapper/url_stat.md) — Support for stat().
- [dir_opendir()](DrupalLocalStreamWrapper/dir_opendir.md) — Support for opendir().
- [dir_readdir()](DrupalLocalStreamWrapper/dir_readdir.md) — Support for readdir().
- [dir_rewinddir()](DrupalLocalStreamWrapper/dir_rewinddir.md) — Support for rewinddir().
- [dir_closedir()](DrupalLocalStreamWrapper/dir_closedir.md) — Support for closedir().

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
