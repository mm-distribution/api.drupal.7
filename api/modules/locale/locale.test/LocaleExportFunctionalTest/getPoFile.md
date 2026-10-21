# LocaleExportFunctionalTest::getPoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1413–1426 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1413-L1426)
- **Class:** [LocaleExportFunctionalTest](../LocaleExportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFile()
```

## Documentation

```text
Helper function that returns a proper .po file.
```

## Code

```php
  function getPoFile() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 6\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

msgid "Monday"
msgstr "lundi"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
