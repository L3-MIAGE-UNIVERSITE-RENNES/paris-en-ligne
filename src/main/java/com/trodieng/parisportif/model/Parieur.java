package com.trodieng.parisportif.model;

import javax.persistence.*;

import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class Parieur extends Identifiable  {
	String nom;
	String email;
	String motDePasse;
	int jeton;

}
