# LocaleImportFunctionalTest::getPoFileWithMissingPlural()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1314–1326 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1314-L1326)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFileWithMissingPlural()
```

## Documentation

```text
Returns a .po file with a missing plural formula.
```

## Code

```php
  function getPoFileWithMissingPlural() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

msgid "Monday"
msgstr "Ponedjeljak"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
