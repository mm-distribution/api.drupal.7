# Manager::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Manager.php`](../_file.md), lines 113–116 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Manager.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php#L113-L116)
- **Class:** [Manager](../Manager.md)

## Signature

```php
public function assert($path, $command)
```

## Documentation

```text
@param string $path
@param string $command
@return bool
```

## Code

```php
    public function assert($path, $command)
    {
        return $this->behavior->assert($path, $command);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Manager.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php) · Licensed GPL-2.0-or-later (see LICENSE)._
