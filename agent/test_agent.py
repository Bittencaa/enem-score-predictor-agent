from tools import predict_enem_score


def test_good_school():
    """Nível 1 — cenário favorável"""
    score = predict_enem_score(
        nu_ano=2022,
        nu_matriculas=800,
        nu_participantes=600,
        nu_taxa_aprovacao=95.0,
        nu_taxa_reprovacao=3.0,
        nu_taxa_abandono=2.0,
        tp_dependencia_adm_escola=2,  # estadual
        tp_localizacao_escola=1,      # urbana
        porte_escola="Maior que 90 alunos",
        sg_uf_escola="SP"
    )

    print("Good school score:", score)


def test_bad_school():
    """Nível 1 — cenário desfavorável"""
    score = predict_enem_score(
        nu_ano=2022,
        nu_matriculas=100,
        nu_participantes=20,
        nu_taxa_aprovacao=50.0,
        nu_taxa_reprovacao=30.0,
        nu_taxa_abandono=20.0,
        tp_dependencia_adm_escola=4,  # privada
        tp_localizacao_escola=2,      # rural
        porte_escola="De 1 a 30 alunos",
        sg_uf_escola="RO"
    )

    print("Bad school score:", score)


def test_sensitivity_aprovacao():
    """Nível 2 — sensibilidade à taxa de aprovação"""
    print("\nSensitivity test (approval rate):")

    for aprovacao in [60, 70, 80, 90]:
        score = predict_enem_score(
            nu_ano=2022,
            nu_matriculas=500,
            nu_participantes=200,
            nu_taxa_aprovacao=aprovacao,
            nu_taxa_reprovacao=100 - aprovacao,
            nu_taxa_abandono=0,
            tp_dependencia_adm_escola=2,
            tp_localizacao_escola=1,
            porte_escola="Maior que 90 alunos",
            sg_uf_escola="SP"
        )

        print(f"Aprovação {aprovacao}% → Score {score}")


def test_edge_case_min_values():
    """Teste de limite — valores mínimos plausíveis"""
    score = predict_enem_score(
        nu_ano=2022,
        nu_matriculas=1,
        nu_participantes=1,
        nu_taxa_aprovacao=0.0,
        nu_taxa_reprovacao=100.0,
        nu_taxa_abandono=0.0,
        tp_dependencia_adm_escola=2,
        tp_localizacao_escola=2,
        porte_escola="De 1 a 30 alunos",
        sg_uf_escola="AC"
    )

    print("\nEdge case (minimum values) score:", score)


if __name__ == "__main__":
    print("Running ENEM model tests...\n")

    test_good_school()
    test_bad_school()
    test_sensitivity_aprovacao()
    test_edge_case_min_values()

    print("\nAll tests executed successfully.")
