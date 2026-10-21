# PharStreamWrapper

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](_file.md), lines 16–500 · [local source](../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L16-L500)

## Signature

```php
class PharStreamWrapper
```

## Documentation

_No docblock in source._

## Constants

### STREAM_OPEN_FOR_INCLUDE

```php
const STREAM_OPEN_FOR_INCLUDE = 128;
```

```text
Internal stream constants that are not exposed to PHP, but used...
@see https://github.com/php/php-src/blob/e17fc0d73c611ad0207cac8a4a01ded38251a7dc/main/php_streams.h
```

## Properties

### $context

```php
public $context;
```

```text
@var resource
```

### $internalResource

```php
protected $internalResource;
```

```text
@var resource
```

### $invocation

```php
protected $invocation;
```

```text
@var PharInvocation
```

## Methods (derived index)

- [dir_closedir()](PharStreamWrapper/dir_closedir.md)
- [dir_opendir()](PharStreamWrapper/dir_opendir.md)
- [dir_readdir()](PharStreamWrapper/dir_readdir.md)
- [dir_rewinddir()](PharStreamWrapper/dir_rewinddir.md)
- [mkdir()](PharStreamWrapper/mkdir.md)
- [rename()](PharStreamWrapper/rename.md)
- [rmdir()](PharStreamWrapper/rmdir.md)
- [stream_close()](PharStreamWrapper/stream_close.md)
- [stream_eof()](PharStreamWrapper/stream_eof.md)
- [stream_flush()](PharStreamWrapper/stream_flush.md)
- [stream_lock()](PharStreamWrapper/stream_lock.md)
- [stream_metadata()](PharStreamWrapper/stream_metadata.md)
- [stream_open()](PharStreamWrapper/stream_open.md)
- [stream_read()](PharStreamWrapper/stream_read.md)
- [stream_seek()](PharStreamWrapper/stream_seek.md)
- [stream_set_option()](PharStreamWrapper/stream_set_option.md)
- [stream_stat()](PharStreamWrapper/stream_stat.md)
- [stream_tell()](PharStreamWrapper/stream_tell.md)
- [stream_truncate()](PharStreamWrapper/stream_truncate.md)
- [stream_write()](PharStreamWrapper/stream_write.md)
- [unlink()](PharStreamWrapper/unlink.md)
- [url_stat()](PharStreamWrapper/url_stat.md)
- [assert()](PharStreamWrapper/assert.md)
- [collectInvocation()](PharStreamWrapper/collectInvocation.md)
- [resolveAssertable()](PharStreamWrapper/resolveAssertable.md)
- [invokeInternalStreamWrapper()](PharStreamWrapper/invokeInternalStreamWrapper.md) — Invokes commands on the native PHP Phar stream wrapper.
- [restoreInternalSteamWrapper()](PharStreamWrapper/restoreInternalSteamWrapper.md)
- [registerStreamWrapper()](PharStreamWrapper/registerStreamWrapper.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
