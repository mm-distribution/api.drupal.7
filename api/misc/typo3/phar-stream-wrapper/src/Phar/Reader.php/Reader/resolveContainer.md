# Reader::resolveContainer()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 50–81 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L50-L81)
- **Class:** [Reader](../Reader.md)

## Signature

```php
public function resolveContainer()
```

## Documentation

```text
@return Container
```

## Code

```php
    public function resolveContainer()
    {
        $data = $this->extractData($this->resolveStream() . $this->fileName);

        if ($data['stubContent'] === null) {
            throw new ReaderException(
                'Cannot resolve stub',
                1547807881
            );
        }
        if ($data['manifestContent'] === null || $data['manifestLength'] === null) {
            throw new ReaderException(
                'Cannot resolve manifest',
                1547807882
            );
        }
        if (strlen($data['manifestContent']) < $data['manifestLength']) {
            throw new ReaderException(
                sprintf(
                    'Exected manifest length %d, got %d',
                    strlen($data['manifestContent']),
                    $data['manifestLength']
                ),
                1547807883
            );
        }

        return new Container(
            Stub::fromContent($data['stubContent']),
            Manifest::fromContent($data['manifestContent'])
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
