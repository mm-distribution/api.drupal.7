# includes/stream_wrappers.inc

- **Source:** [local](../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · 1010 lines

## File documentation

```text
@file
Drupal stream wrapper interface.

Provides a Drupal interface and classes to implement PHP stream wrappers for
public, private, and temporary files.

A stream wrapper is an abstraction of a file system that allows Drupal to
use the same set of methods to access both local files and remote resources.

Note that PHP 5.2 fopen() only supports URIs of the form "scheme://target"
despite the fact that according to RFC 3986 a URI's scheme component
delimiter is in general just ":", not "://".  Because of this PHP limitation
and for consistency Drupal will only accept URIs of form "scheme://target".

@see http://www.faqs.org/rfcs/rfc3986.html
@see http://bugs.php.net/bug.php?id=47070
```

## Classes and interfaces (derived index)

- [StreamWrapperInterface](StreamWrapperInterface.md) — Generic PHP stream wrapper interface.
- [DrupalStreamWrapperInterface](DrupalStreamWrapperInterface.md) — Drupal stream wrapper extension.
- [DrupalLocalStreamWrapper](DrupalLocalStreamWrapper.md) — Drupal stream wrapper base class for local files.
- [DrupalPublicStreamWrapper](DrupalPublicStreamWrapper.md) — Drupal public (public://) stream wrapper class.
- [DrupalPrivateStreamWrapper](DrupalPrivateStreamWrapper.md) — Drupal private (private://) stream wrapper class.
- [DrupalTemporaryStreamWrapper](DrupalTemporaryStreamWrapper.md) — Drupal temporary (temporary://) stream wrapper class.

## Constants

### STREAM_WRAPPERS_ALL

- Line 32

```php
define('STREAM_WRAPPERS_ALL', 0x0000);
```

```text
Stream wrapper bit flag -- a filter that matches all wrappers.
```

### STREAM_WRAPPERS_LOCAL

- Line 37

```php
define('STREAM_WRAPPERS_LOCAL', 0x0001);
```

```text
Stream wrapper bit flag -- refers to a local file system location.
```

### STREAM_WRAPPERS_READ

- Line 42

```php
define('STREAM_WRAPPERS_READ', 0x0004);
```

```text
Stream wrapper bit flag -- wrapper is readable (almost always true).
```

### STREAM_WRAPPERS_WRITE

- Line 47

```php
define('STREAM_WRAPPERS_WRITE', 0x0008);
```

```text
Stream wrapper bit flag -- wrapper is writeable.
```

### STREAM_WRAPPERS_VISIBLE

- Line 52

```php
define('STREAM_WRAPPERS_VISIBLE', 0x0010);
```

```text
Stream wrapper bit flag -- exposed in the UI and potentially web accessible.
```

### STREAM_WRAPPERS_HIDDEN

- Line 62

```php
define('STREAM_WRAPPERS_HIDDEN', STREAM_WRAPPERS_READ | STREAM_WRAPPERS_WRITE);
```

```text
Stream wrapper type flag -- not visible in the UI or accessible via web,
but readable and writable. E.g. the temporary directory for uploads.
```

### STREAM_WRAPPERS_LOCAL_HIDDEN

- Line 67

```php
define('STREAM_WRAPPERS_LOCAL_HIDDEN', STREAM_WRAPPERS_LOCAL | STREAM_WRAPPERS_HIDDEN);
```

```text
Stream wrapper type flag -- hidden, readable and writeable using local files.
```

### STREAM_WRAPPERS_WRITE_VISIBLE

- Line 72

```php
define('STREAM_WRAPPERS_WRITE_VISIBLE', STREAM_WRAPPERS_READ | STREAM_WRAPPERS_WRITE | STREAM_WRAPPERS_VISIBLE);
```

```text
Stream wrapper type flag -- visible, readable and writeable.
```

### STREAM_WRAPPERS_READ_VISIBLE

- Line 77

```php
define('STREAM_WRAPPERS_READ_VISIBLE', STREAM_WRAPPERS_READ | STREAM_WRAPPERS_VISIBLE);
```

```text
Stream wrapper type flag -- visible and read-only.
```

### STREAM_WRAPPERS_NORMAL

- Line 86

```php
define('STREAM_WRAPPERS_NORMAL', STREAM_WRAPPERS_WRITE_VISIBLE);
```

```text
Stream wrapper type flag -- the default when 'type' is omitted from
hook_stream_wrappers(). This does not include STREAM_WRAPPERS_LOCAL,
because PHP grants a greater trust level to local files (for example, they
can be used in an "include" statement, regardless of the "allow_url_include"
setting), so stream wrappers need to explicitly opt-in to this.
```

### STREAM_WRAPPERS_LOCAL_NORMAL

- Line 91

```php
define('STREAM_WRAPPERS_LOCAL_NORMAL', STREAM_WRAPPERS_LOCAL | STREAM_WRAPPERS_NORMAL);
```

```text
Stream wrapper type flag -- visible, readable and writeable using local files.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
