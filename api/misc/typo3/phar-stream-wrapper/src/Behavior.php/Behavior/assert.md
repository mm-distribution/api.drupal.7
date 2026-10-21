# Behavior::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](../_file.md), lines 67–73 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L67-L73)
- **Class:** [Behavior](../Behavior.md)

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
        $this->assertCommand($command);
        $this->assertAssertionCompleteness();

        return $this->assertions[$command]->assert($path, $command);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
