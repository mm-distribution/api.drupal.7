# Behavior

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](_file.md), lines 14–124 · [local source](../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L14-L124)

## Signature

```php
class Behavior implements Assertable
```

## Documentation

_No docblock in source._

## Constants

### COMMAND_DIR_OPENDIR

```php
const COMMAND_DIR_OPENDIR = 'dir_opendir';
```

### COMMAND_MKDIR

```php
const COMMAND_MKDIR = 'mkdir';
```

### COMMAND_RENAME

```php
const COMMAND_RENAME = 'rename';
```

### COMMAND_RMDIR

```php
const COMMAND_RMDIR = 'rmdir';
```

### COMMAND_STEAM_METADATA

```php
const COMMAND_STEAM_METADATA = 'stream_metadata';
```

### COMMAND_STREAM_OPEN

```php
const COMMAND_STREAM_OPEN = 'stream_open';
```

### COMMAND_UNLINK

```php
const COMMAND_UNLINK = 'unlink';
```

### COMMAND_URL_STAT

```php
const COMMAND_URL_STAT = 'url_stat';
```

## Properties

### $availableCommands

```php
private $availableCommands = array(
        self::COMMAND_DIR_OPENDIR,
        self::COMMAND_MKDIR,
        self::COMMAND_RENAME,
        self::COMMAND_RMDIR,
        self::COMMAND_STEAM_METADATA,
        self::COMMAND_STREAM_OPEN,
        self::COMMAND_UNLINK,
        self::COMMAND_URL_STAT,
    );
```

```text
@var string[]
```

### $assertions

```php
private $assertions;
```

```text
@var Assertable[]
```

## Methods (derived index)

- [withAssertion()](Behavior/withAssertion.md)
- [assert()](Behavior/assert.md)
- [assertCommands()](Behavior/assertCommands.md)
- [assertCommand()](Behavior/assertCommand.md)
- [assertAssertionCompleteness()](Behavior/assertAssertionCompleteness.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
