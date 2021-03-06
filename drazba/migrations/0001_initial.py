# Generated by Django 4.0.2 on 2022-04-17 15:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Misto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(error_messages={'blank': 'Jméno města/obce musí být vyplněno'}, help_text='Zadejte jméno města/obce', max_length=50, verbose_name='Jméno města/obce')),
                ('psc', models.PositiveIntegerField(help_text='Zadejte poštovní směrovací číslo (bez mezery)', validators=[django.core.validators.RegexValidator('^\\d{5}$', 'Nesprávně zadané poštovní směrovací číslo')], verbose_name='PSČ')),
            ],
            options={
                'verbose_name': 'Město/obec',
                'verbose_name_plural': 'Místa',
                'ordering': ['jmeno'],
            },
        ),
        migrations.CreateModel(
            name='Urad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(error_messages={'blank': 'Název úřadu musí být vyplněn'}, help_text='Zadejte úplný název exekutorského úřadu', max_length=100, verbose_name='Název úřadu')),
                ('adresa', models.CharField(error_messages={'blank': 'Adresa úřadu musí být vyplněna'}, help_text='Zadejte adresu exekutorského úřadu včetně čísla popisného/orientačního', max_length=100, verbose_name='Adresa úřadu')),
                ('mesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drazba.misto', verbose_name='Město')),
            ],
            options={
                'verbose_name': 'Exekutorský úřad',
                'verbose_name_plural': 'Exekutorské úřady',
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaceni', models.CharField(help_text='Zadejte vhodné označení předmětu exekuce', max_length=200, verbose_name='Označení předmětu exekuce')),
                ('cislo_jednaci', models.CharField(help_text='Zadejte přesné číslo jednací', max_length=20, verbose_name='Číslo jednací')),
                ('popis', models.TextField(help_text='Zadejte podrobnější popis předmětu dražby', verbose_name='Popis předmětu dražby')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fota', verbose_name='Fotografie')),
                ('pocatecni_cena', models.PositiveIntegerField(verbose_name='Počáteční cena v Kč')),
                ('zacatek_drazby', models.DateTimeField(verbose_name='Datum a čas začátku dražby')),
                ('konec_drazby', models.DateTimeField(verbose_name='Datum a čas konce dražby')),
                ('misto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drazba.misto', verbose_name='Místo')),
            ],
            options={
                'verbose_name': 'Předmět dražby',
                'verbose_name_plural': 'Předměty dražby',
                'ordering': ['zacatek_drazby'],
            },
        ),
        migrations.CreateModel(
            name='Exekutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(error_messages={'blank': 'Jméno exekutora musí být vyplněno'}, help_text='Zadejte jméno exekutora', max_length=50, verbose_name='Jméno exekutora')),
                ('prijmeni', models.CharField(error_messages={'blank': 'Příjmení exekutora musí být vyplněno'}, help_text='Zadejte příjmení exekutora', max_length=50, verbose_name='Příjmení exekutora')),
                ('titul', models.CharField(blank=True, choices=[('Bc.', 'Bc.'), ('Ing.', 'Ing.'), ('Mgr.', 'Mgr.'), ('JUDr.', 'JUDr.')], help_text='Zvolte titul exekutora', max_length=5, null=True, verbose_name='Titul')),
                ('email', models.EmailField(error_messages={'blank': 'Pole nesmí být prázdné', 'invalid': 'Neplatná e-mailová adresa', 'unique': 'E-mailová adresa musí být jedinečná'}, help_text='Zadejte e-mail exekutora', max_length=254, unique=True, verbose_name='Email exekutora')),
                ('telefon', models.CharField(blank=True, help_text='Zadejte telefon v podobě: +420 777 777 777', max_length=16, validators=[django.core.validators.RegexValidator('^[+]\\d{3}( \\d{3}){3}$', 'Nesprávně zadané telefonní číslo')], verbose_name='Telefon exekutora')),
                ('urad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drazba.urad', verbose_name='Exekutorský úřad')),
            ],
            options={
                'verbose_name': 'Exekutor',
                'verbose_name_plural': 'Exekutoři',
                'ordering': ['prijmeni', 'jmeno'],
            },
        ),
    ]
