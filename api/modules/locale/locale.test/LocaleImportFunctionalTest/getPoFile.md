# LocaleImportFunctionalTest::getPoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1161–1197 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1161-L1197)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
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
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

msgid "One sheep"
msgid_plural "@count sheep"
msgstr[0] "un mouton"
msgstr[1] "@count moutons"

msgid "Monday"
msgstr "lundi"

msgid "Tuesday"
msgstr "mardi"

msgid "Wednesday"
msgstr "mercredi"

msgid "Thursday"
msgstr "jeudi"

msgid "Friday"
msgstr "vendredi"

msgid "Saturday"
msgstr "samedi"

msgid "Sunday"
msgstr "dimanche"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
