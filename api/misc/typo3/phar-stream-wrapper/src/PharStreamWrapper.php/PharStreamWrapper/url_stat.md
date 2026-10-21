# PharStreamWrapper::url_stat()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 395–400 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L395-L400)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function url_stat($path, $flags)
```

## Documentation

```text
@param string $path
@param int $flags
@return array|false
```

## Code

```php
    public function url_stat($path, $flags)
    {
        $this->assert($path, Behavior::COMMAND_URL_STAT);
        $functionName = $flags & STREAM_URL_STAT_QUIET ? '@stat' : 'stat';
        return $this->invokeInternalStreamWrapper($functionName, $path);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
